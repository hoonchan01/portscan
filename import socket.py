import socket

def get_local_ip():
    hostname = socket.gethostname()  # 컴퓨터 이름
    local_ip = socket.gethostbyname(hostname)  # IP 주소 얻기
    return local_ip

print(f"현재 로컬 IP 주소: {get_local_ip()}")

def scan_ports(ip, start_port, end_port, port_num=0, opened_port=0): 
    print(f" 스캔 대상: {ip}")
    print(f" 스캔 범위: {start_port} ~ {end_port}\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET: IPv4, socket.SOCK_STRAM: TCP포트
        sock.settimeout(0.5)  # 응답 대기 시간 설정

        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"포트 {port} 열림")
            opened_port = port
            port_num = port_num + 1
        sock.close()
    print(f"총 {port_num}개의 포트가 열렸습니다.\n열린 포트는{opened_port}입니다.")

# 예시 실행
if __name__ == "__main__":
    my_ip = get_local_ip()
    start = int(input("시작 포트 번호: "))
    end = int(input("끝 포트 번호: "))
    scan_ports(my_ip, start, end)