# BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE를 뽑아줘 ~
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
# BOOK 테이블에서
FROM BOOK
# PUBLISHED_DATE의 Y가 2021이고
WHERE DATE_FORMAT(PUBLISHED_DATE, '%Y') = '2021'
# CATEGORY가 '인문'인
AND CATEGORY = '인문'