SELECT COUNT(*) AS COUNT
FROM (
    SELECT ID, REVERSE(CAST(BIN(GENOTYPE) AS CHAR)) AS BIN_GEN
    FROM ECOLI_DATA
) AS TT
WHERE (BIN_GEN LIKE '1%' OR BIN_GEN LIKE '__1%') 
    AND (NOT BIN_GEN LIKE '_1%')