# YOLOv8_mem_utilization

## 1. obb_gpu_memory.py(nvidia-smi)

  ### subprocess.run
  
  Python에서 외부 명령어를 실행하고 그 결과를 캡쳐하기 위한 함수이다. 
  
  #### (1) nvidia-smi : NVIDIA GPU와 관련된 상태를 보여줌
  #### (2) --query-gpu=memory.used : GPU 메모리 사용량 쿼리
  #### (3) --format=csv, nounits, noheader : 출력형식 지정
  #### (4) stdout=subprocess.PIPE : 명령어의 출력 내용을 파이썬 프로세스의 표준 출력으로 설정

  ### result.stdout
  
  명령어가 실행된 후 출력된 데이터

## 2. obb_memory.py(psutil)

  ### psutil

  시스템 및 프로세스 유틸리티 라이브러리, CPU와 메모리, 디스크 등의 자원 사용량을 모니텅링 하고 관리
  
  #### (1) process = psutil.Process(os.getpid()) : 현재 실행 중인 PID 반환해서 이 프로세스에 해당하는 정보를 담은 객체를 생성
  #### (2) mem_info = process.memory_info() : 해당 프로세스의 메모리 사용 정보 반환. rss, vms 등
  #### (3) return mem_info.rss / (1024 ** 2) : rss(Resident Set Size)를 바이트 단위로 반환 후 MB 단위로 변환
