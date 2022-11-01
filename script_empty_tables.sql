create table product (
product_id text,
product_name text,
product_category text,
price text
);

create table total_order_yearly (
order_date text,
total_order int
);

create table total_order_product_yearly (
order_date text,
product_id text,
total_order int
);