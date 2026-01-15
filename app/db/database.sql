create database peluqueria;
use peluqueria;

create table usuario (
	id int auto_increment primary key,
    Nombre varchar(50),
    Apellido varchar(50),
    Numero varchar(50) UNIQUE,
    correo varchar(50) UNIQUE ,
    password VARCHAR(100) NOT NULL,
	activo BOOLEAN DEFAULT TRUE,
	rol VARCHAR(20) DEFAULT 'admin'
    );

create table clientes (
    id int auto_increment primary key,
    Nombre varchar(50),
    Apellido varchar(50),
    Numero varchar(50) unique,
    correo varchar(50) unique
); 

create table servicios (
	id int auto_increment primary key,
	nombre varchar(50),
    precio Decimal(10,2),
    estado boolean default true,
    fecha date
    );
    
create table ventas (
	id int auto_increment primary key,
    usuario_id int,
    cliente_id int,
    servicio_id int,
    precio_final Decimal(10,2),
    fecha date,
    
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (servicio_id) REFERENCES servicios(id)
    );
    
-- datos de prueba:

INSERT INTO usuario (Nombre, Apellido, Numero, correo, password, rol)
VALUES
('Miguel', 'Rodriguez', '3001234567', 'miguel@peluqueria.com', 'hash123', 'admin'),
('Carlos', 'Lopez', '3017654321', 'carlos@peluqueria.com', 'hash456', 'empleado');

INSERT INTO clientes (Nombre, Apellido, Numero, correo)
VALUES
('Juan', 'Perez', '3101112233', 'juan@gmail.com'),
('Ana', 'Gomez', '3124445566', 'ana@gmail.com'),
('Pedro', 'Martinez', '3137778899', 'pedro@gmail.com');

INSERT INTO servicios (nombre, precio, estado, fecha)
VALUES
('Corte', 15000.00, true, CURDATE()),
('Corte + Barba', 25000.00, true, CURDATE()),
('Tintura', 40000.00, true, CURDATE());

INSERT INTO ventas (usuario_id, cliente_id, servicio_id, precio_final, fecha)
VALUES
(1, 1, 1, 15000.00, CURDATE()),
(2, 2, 2, 25000.00, CURDATE()),
(1, NULL, 3, 40000.00, CURDATE());

-- consultas tipo join de prueba 

-- todas las ventas con usuarios y servicios
SELECT 
    v.id AS venta_id,
    u.Nombre AS usuario,
    s.nombre AS servicio,
    v.precio_final,
    v.fecha
FROM ventas v
JOIN usuario u ON v.usuario_id = u.id
JOIN servicios s ON v.servicio_id = s.id;


-- servicios mas vendidos
SELECT
    s.nombre AS servicio,
    COUNT(v.id) AS cantidad_vendida,
    SUM(v.precio_final) AS total_generado
FROM ventas v
JOIN servicios s ON v.servicio_id = s.id
GROUP BY s.nombre;

-- ventas por clientes registrados
SELECT
    c.Nombre AS cliente,
    COUNT(v.id) AS total_servicios,
    SUM(v.precio_final) AS total_gastado
FROM ventas v
JOIN clientes c ON v.cliente_id = c.id
GROUP BY c.Nombre;



