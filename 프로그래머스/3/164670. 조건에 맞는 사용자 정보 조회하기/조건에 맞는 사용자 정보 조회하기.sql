-- 코드를 입력하세요
# 1-1. SUBQUERY - 복수(다중)행 -> IN
# 1-2. GROUP BY + HAVING 절을 통하여 3건 이상 등록한 사용자(WRITER_ID) 추출
# 2-1. CONCAT(문자열1, 문자열2, ...) 를 통하여 문자열 합치기 
# 2-2. SUBSTR(문자열, 시작 위치, 길이) 를 통하여 전화번호 나누고 하이픈 '-' 추가
# 3. ORDER BY 회원ID(USER_ID)로 내림차순 정렬 

SELECT USER_ID,
    NICKNAME,
    CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS 전체주소,
    CONCAT(SUBSTR(TLNO, 1, 3), '-', SUBSTR(TLNO, 4, 4), '-', SUBSTR(TLNO, 8, 4)) AS 전화번호
FROM USED_GOODS_USER
WHERE USER_ID IN (SELECT WRITER_ID
      FROM USED_GOODS_BOARD
      GROUP BY WRITER_ID
      HAVING COUNT(*) >= 3)
ORDER BY USER_ID DESC 