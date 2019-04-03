CREATE DATABASE pdd;
USE pdd;

CREATE TABLE orders(
id INT auto_increment PRIMARY KEY NOT NULL,
order_time VARCHAR(20),
cate VARCHAR(20),
goods_id VARCHAR(5),
order_amount DECIMAL
);

# 统计2018各月销售金额
SELECT
	sum( t.order_amount ) sumamount,
	t.time 
FROM
	( SELECT SUBSTR( order_time, 1, 7 ) time, order_amount FROM orders ) t 
GROUP BY
	t.time;
	
	
# 统计2018各月销售金额，并排名
SELECT
	a.*,
	@curRank := @curRank + 1 AS rank 
FROM
	(
SELECT
	sum( t.order_amount ) sumamount,
	t.time 
FROM
	( SELECT SUBSTR( order_time, 1, 7 ) time, order_amount FROM orders ) t 
GROUP BY
	t.time 
	) a,
	( SELECT @curRank := 0 ) b
ORDER BY
	sumamount;
	
# 选出2月每个类目销量最高的两个爆款以及排名先后
SELECT
	b.*,
	@curRank := @curRank + 1 AS rank 
FROM
	(
SELECT
	a.cate,
	a.goods_id,
	a.sumamount 
FROM
	(
SELECT
	cate,
	goods_id,
	sum( order_amount ) sumamount 
FROM
	orders 
WHERE
	substr( order_time, 1, 7 ) = '2018-02' 
GROUP BY
	cate,
	goods_id 
ORDER BY
	cate,
	sumamount DESC 
	) a 
WHERE
	( SELECT count( * ) FROM orders WHERE goods_id = a.goods_id AND order_amount > a.sumamount ) < 2 
ORDER BY
	cate,
	sumamount DESC 
	) b,
	( SELECT @curRank := 0 ) c 
ORDER BY
	sumamount DESC;
