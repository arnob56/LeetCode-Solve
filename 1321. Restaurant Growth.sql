# Write your MySQL query statement below
WITH DailySum AS (
    SELECT 
        visited_on,
        SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),
SevenDayWindow AS (
    SELECT 
        a.visited_on,
        SUM(b.amount) AS amount,
        ROUND(SUM(b.amount) / 7, 2) AS average_amount
    FROM DailySum a
    JOIN DailySum b
        ON DATEDIFF(a.visited_on, b.visited_on) BETWEEN 0 AND 6
    GROUP BY a.visited_on
)
SELECT 
    visited_on,
    amount,
    average_amount
FROM SevenDayWindow
WHERE visited_on >= (
    SELECT MIN(visited_on) FROM DailySum
) + INTERVAL 6 DAY
ORDER BY visited_on;
