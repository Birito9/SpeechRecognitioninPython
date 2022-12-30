DROP TABLE sinhvien;
drop table quantrivien;

create table SINHVIEN
(
MaSV char(11) not null primary key,
HoSV nvarchar(20) not null,
TenSV nvarchar(10)not null,
Phai nchar(7),
NgaySinh nvarchar(20) not null,
NoiSinh nvarchar (20),
Nganh nvarchar(30),
HeDaoTao nvarchar(10),
NamNhapHoc char(5)
);

create table QUANTRIVIEN
(
MaQTV char(11) not null primary key,
HoNV nvarchar(20) not null,
TenNV nvarchar(10)not null,
Phai nchar(7),
NgaySinh nvarchar(20) not null,
NoiSinh nvarchar (20)
);

CREATE TABLE tuvantuyensinh ( 
  MaTuKhoa int (11) AUTO_INCREMENT,
  TuKhoa nvarchar (150) DEFAULT NULL,
  CauTraLoi nvarchar(4000) DEFAULT NULL,   
PRIMARY KEY (MaTuKhoa) 
); 
select * from quantrivien;
select * from sinhvien 
where MaSV = 'DH51903096';


Insert into SINHVIEN values('DH51903096','Nguyễn Thanh','Bằng','Nam','23/02/2001','Hồ Chí Minh','Công Nghệ Thông Tin', 'Đại Học', '2019');
Insert into SINHVIEN values('DH51903097','Nguyễn Văn Thanh','Đức','Nam','29/07/2001','Hồ Chí Minh','Thiết Kế', 'Đại Học', '2021');
Insert into SINHVIEN values('DH51903098','Huỳnh Quốc','Huy','Nam','13/08/2001','Hồ Chí Minh','Công Nghệ Thông Tin', 'Cao Đẳng', '2019');
Insert into SINHVIEN values('DH51903099','Mai Hoàng','Khang','Nam','16/09/2001','Hồ Chí Minh','Quản Trị Kinh Doanh', 'Đại Học', '2020');
Insert into SINHVIEN values('DH51903100','Nguyễn Trung','Kiên','Nam','12/11/2001','Hồ Chí Minh','Cơ Khí', 'Đại Học', '2018');
Insert into quantrivien values('QTV01','Nguyễn Thanh','Bằng','Nam','23/02/2001','Hồ Chí Minh');

select * from sinhvien
where HoSV like N'Nguyễn Văn Thanh' and TenSV like N'Đức' and Nganh like N'Thiết Kế';

UPDATE SINHVIEN
SET HoSV = 'Nguyễn Văn', TenSV = 'Thanh', Phai = 'Nữ', NgaySinh = '14/09/2001', NoiSinh = 'Hà Nội'
WHERE MaSV = 'DH51903097';

DELETE from sinhvien 
where MaSV = 'DH51923096';

select * from sinhvien where MaSV = 'DH51903096';

SET @MSSV = 'DH51903097', @HoSV = N'Huỳnh Văn', @TenSV = N'Thanh', @Phai = 'Nam', @NgaySinh = '24/06/2001', @NoiSinh = 'Hà Nội';
CALL SUASINHVIEN(@MSSV, @HoSV, @TenSV, @Phai, @NgaySinh, @NoiSinh);
SELECT @MSSV;

