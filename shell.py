import subprocess
import pathlib
path = pathlib.Path().resolve()
import threading
import queue
import gc
def read_output(pipe, q , stop_event):
    while not stop_event.is_set():
            output = pipe.readline()
            if output:
                q.put(output)
            else: 
                break
    pipe.close()
    q.put(None)  

def write_logs_and_output(q):
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        while True:
            if not q.empty():
                line = q.get()
                if line is None: break
                if( (f"{path.resolve()}") in line ) and ("exit" in line or "EXIT" in line or "files" in line): continue
                log_file.write(line)
                log_file.flush()
                print(line, end='')

def startShell(command):
    stop_event = threading.Event()
    p = subprocess.Popen(f'cmd.exe /K cd files && {command}', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    output_queue = queue.Queue()

    output_thread = threading.Thread(target=read_output, args=(p.stdout, output_queue , stop_event))
    output_thread.start()

    log_thread = threading.Thread(target=write_logs_and_output, args=(output_queue,))
    log_thread.daemon = True
    log_thread.start()

    rerun = False
    with open('log.txt', 'a') as log_file:
        log_file.write(f"{path.resolve()}"+">"+command+"\n")

    with open('log.txt', 'a') as log_file:
        try:
            while True:
                inp = input()
                if inp.strip().lower() == 'exit':  
                    log_file.write(f"{"--"*20}FILE{"--"*20}\n")
                    p.stdin.write('exit\n')
                    p.stdin.flush()
                    break   
                if inp.strip().lower() == 'rerun':
                    rerun = True
                    raise KeyboardInterrupt
                
                log_file.write(f"{inp}\n")
                log_file.flush()
                p.stdin.write(inp + '\n')
                p.stdin.flush()

        except KeyboardInterrupt:
            pass

        finally:
            stop_event.set()
            if p.stdin:
                p.stdin.close()
            if p.stdout:
                p.stdout.close()
            p.terminate()
            p.wait() 
            
            output_queue.put(None)  
            output_thread.join()  
            log_thread.join() 

            gc.collect()
            if(rerun == True):
                startShell(command)