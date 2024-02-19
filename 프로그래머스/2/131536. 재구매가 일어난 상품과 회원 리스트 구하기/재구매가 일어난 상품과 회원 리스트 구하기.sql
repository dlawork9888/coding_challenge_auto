# 재구매한 회원 ID, 재구매한 상품 ID
# USER_ID, PRODUCT_ID	

SELECT USER_ID, PRODUCT_ID
    FROM ONLINE_SALE
        GROUP BY USER_ID, PRODUCT_ID HAVING COUNT(ONLINE_SALE_ID) >= 2
        ORDER BY USER_ID ASC, PRODUCT_ID DESC