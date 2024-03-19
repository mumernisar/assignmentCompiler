import subprocess
import threading
import queue
import pathlib
path = pathlib.Path().resolve()

def read_output(pipe, q):
    while True:
        output = pipe.readline()
        q.put(output)
        if not output:
            break

def write_logs_and_output(q):
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        while True:
            if not q.empty():
                line = q.get()
                if( (f"{path.resolve()}") in line ) and ("exit" in line or "EXIT" in line or "files" in line): continue
                log_file.write(line)
                log_file.flush()
                print(line, end='')

def startShell(command):
    p = subprocess.Popen(f'cmd.exe /K cd files && {command}', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    output_queue = queue.Queue()

    output_thread = threading.Thread(target=read_output, args=(p.stdout, output_queue))
    output_thread.daemon = True
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
            p.terminate()
            if(rerun == True):
                startShell(command)