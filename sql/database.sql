CREATE DATABASE pboperpus;
USE pboperpus;

CREATE TABLE tbl_user(
  id_user VARCHAR(25) PRIMARY KEY NOT NULL,
  nama_depan VARCHAR(100),
  nama_tengah VARCHAR(100),
  nama_belakang VARCHAR(100),
  tipe_user VARCHAR(25),
  username VARCHAR(15),
  password VARCHAR(32)
);

INSERT INTO tbl_user 
VALUE
  ('USER001', 'Andrian', '', 'Maulana', 'Administrator', 'andrian', MD5('12345'));

SELECT * FROM tbl_user;

CREATE TABLE tbl_anggota(
  id_anggota VARCHAR(25) PRIMARY KEY NOT NULL,
  nama_depan VARCHAR(100),
  nama_tengah VARCHAR(100),
  nama_belakang VARCHAR(100),
  jenis_kelamin VARCHAR(15),
  no_telp VARCHAR(20),
  alamat VARCHAR(200),
  email VARCHAR(200)
);

CREATE TABLE tbl_genre(
  id_genre VARCHAR(25) PRIMARY KEY NOT NULL,
  nama_genre VARCHAR(100)
);

CREATE TABLE tbl_penulis(
  id_penulis VARCHAR(25) PRIMARY KEY NOT NULL,
  nama_depan VARCHAR(100),
  nama_tengah VARCHAR(100),
  nama_belakang VARCHAR(100)
);

CREATE TABLE tbl_buku(
  isbn VARCHAR(25) PRIMARY KEY NOT NULL,
  id_genre VARCHAR(25),
  id_penulis VARCHAR(25),
  judul VARCHAR(100),
  penerbit VARCHAR(100),
  tanggal_publikasi DATE,
  jumlah_stok INT,
  Foreign Key (id_genre) REFERENCES tbl_genre(id_genre),
  Foreign Key (id_penulis) REFERENCES tbl_penulis(id_penulis)
);

CREATE TABLE tbl_peminjaman(
  id_peminjaman INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  isbn VARCHAR(25),
  id_anggota VARCHAR(25),
  tanggal_pinjam DATE,
  tanggal_tempo DATE,
  tanggal_kembali DATE,
  Foreign Key (isbn) REFERENCES tbl_buku(isbn),
  Foreign Key (id_anggota) REFERENCES tbl_anggota(id_anggota)
);

SHOW VARIABLES LIKE 'hostname';

SELECT USER();

SELECT @IDENTIFIED_BY_PASSWORD;
