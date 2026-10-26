# 실사용매칭시험 데이터 Analyzer V2.0 ⚡

LG전자 신뢰성 시험 및 실사용 매칭시험 CSV 데이터의 다채널 그래프 시각화 및 통계 분석을 수행하는 Web 애플리케이션입니다.

---

## 🌟 주요 기능
1. **대용량 CSV 고속 로딩**: 브라우저 기반 스트리밍 파싱 기술로 100MB 이상의 대용량 시험 데이터도 지연 없이 즉시 로드 (UTF-8, CP949 자동 판별)
2. **상수 컬럼 자동 필터링**: 모든 값이 동일한 비유효 컬럼을 자동 선별하여 분석 목록에서 제외
3. **인터랙티브 Matplotlib 스타일 차트**:
   - 다중 Y채널 동시 플로팅 지원
   - Home, Pan(이동), Zoom(영역 확대), Wheel Zoom, 마우스 Hover 툴팁 지원
4. **정밀 데이터 통계 분석 출력**:
   - 선택된 X축 시간/구간 범위 기준 통계치 자동 계산
   - `Count`, `Mean`, `Max`, `Max Time`, `Min`, `Min Time`, `Std`, `RMS`, `Range`, `Peak-to-Peak` 실시간 산출
5. **데이터 내보내기**:
   - 현재 확대/선택된 범위만의 CSV 파일 저장 (BOM UTF-8 지원)
   - 200 DPI 고해상도 그래프 JPG 이미지 저장

---

## 📁 저장소 구조
```text
├── .streamlit/
│   └── config.toml                        # (선택) Streamlit 테마 및 서버 설정
├── 02_Matching_Test_Graph_Web_Analyzer.html  # 핵심 분석기 웹 소스코드
├── app.py                                 # Streamlit 엔트리포인트 실행 파일
├── requirements.txt                       # 파이썬 의존성 패키지 목록
└── README.md                              # 프로젝트 설명서