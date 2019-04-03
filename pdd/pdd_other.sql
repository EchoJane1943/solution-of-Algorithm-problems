CREATE TABLE orders ( id INT PRIMARY KEY AUTO_INCREMENT, order_time TIMESTAMP, cate VARCHAR ( 255 ), goods_id INT, order_amount INT );
INSERT INTO orders ( order_time, cate, goods_id, order_amount )
VALUES
	( '2018-02-28 00:00:01', 'fruit', 223, 100 ),
	( '2018-02-28 01:01:01', 'tea', 444, 111 ),
	( '2018-02-28 06:06:06', 'tea', 444, 666 ),
	( '2018-03-01 07:01:10', 'tea', 5555, 170 ),
	( '2018-03-01 08:00:00', 'tea', 5555, 180 ),
	( '2018-03-01 00:00:01', 'tea', 333, 100 ),
	( '2018-03-01 00:00:01', 'tea', 444, 188 ),
	( '2018-03-01 00:00:01', 'digit', 45454, 5399 );
	
	
# 统计2018各月销售金额
SELECT
	DATE_FORMAT( t.order_time, '%Y-%m' ) AS '日期',
	SUM( t.order_amount ) AS '销售金额' 
FROM
	orders t 
WHERE
	YEAR ( t.order_time ) = 2018 
GROUP BY
	MONTH ( t.order_time ) 
	
# 统计2018各月销售金额，并排名
SELECT
	tt.r AS '日期',
	tt.x AS '销售金额',
	tt.j AS '金额排名' 
FROM
	(
SELECT
	a.mon AS r,
	a.sum AS x,
CASE
	
	WHEN @prevRank = a.sum THEN
	@curRank 
	WHEN @prevRank := a.sum THEN
	@curRank := @curRank + 1 
	END AS j 
FROM
	(
	SELECT
		DATE_FORMAT( t.order_time, '%Y-%m' ) AS mon,
		SUM( t.order_amount ) AS sum 
	FROM
		orders t 
	WHERE
		YEAR ( t.order_time ) = 2018 
	GROUP BY
		MONTH ( t.order_time ) 
	ORDER BY
		SUM( t.order_amount ) DESC 
	) a,
	( SELECT @curRank := 0, @prevRank := NULL ) b 
	) tt 
ORDER BY
	tt.r 
	
# 选出2月每个类目销量最高的两个爆款以及排名先后
SELECT
	t.cate AS '类目',
	t.goods_id AS '商品id',
	t.rankNO AS '排名' 
FROM
	(
	SELECT
		a.cate,
		a.goods_id,
		a.count,
		@rank :=
	CASE
			
			WHEN @prevCate = a.cate THEN
			@rank + 1 ELSE 1 
		END AS rankNO,
		@prevCate := a.cate AS type 
	FROM
		(
		SELECT
			t.cate,
			t.goods_id,
			count( goods_id ) AS count 
		FROM
			orders t 
		WHERE
			date_format( t.order_time, '%Y%m%d%H%i%s' ) LIKE "2018%" 
		GROUP BY
			t.goods_id 
		ORDER BY
			t.cate,
			count( t.goods_id ) DESC 
		) AS a,
		( SELECT @rank := 0, @prevCate := '' ) b 
	) t 
WHERE
t.rankNO <= 2
