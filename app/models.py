
from sqlalchemy import Column, DateTime, Integer, Float, String, Date, BOOLEAN, ForeignKey, Enum, func, distinct
from sqlalchemy.orm import relationship
from app import db, app
from datetime import datetime
from flask_login import UserMixin
from enum import Enum as UserEnum


class Student(db.Model):
    __tablename__ = 'Student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(100), nullable=False)
    gioitinh = Column(Enum('Male', 'Female'))
    ngaysinh = Column(Date)
    diachi = Column(String(100))
    email = Column(String(100))
    lophoc_id = Column(Integer, ForeignKey('lophoc.ID_lophoc'), nullable=False)
    def __str__(self):
        return self.ten
class UserRole(UserEnum):
    giaovien = 1
    quantri = 2
    nhanvien = 3
class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    active = Column(BOOLEAN, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    avatar = Column(String(100))
    user_role = Column(Enum(UserRole), default=UserRole.quantri)
class LopHoc(db.Model):
    __tablename__ = 'lophoc'
    ID_lophoc = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    TenLop = Column(String(50), nullable=False)
    hocsinhs = relationship('Student', backref='lophoc', lazy=True)
    soluong = Column(Integer, default=40, nullable=False)
    monhocs = relationship('MonHoc', secondary='monhoc_lophoc', backref='lophocs')

    def __str__(self):
        return self.TenLop

class MonHoc(db.Model):
    __tablename__ = 'monhoc'
    IDMonHoc = Column(Integer, primary_key=True, autoincrement=True)
    TenMH = Column(String(50), nullable=False)
    id_hocky = Column(Integer, ForeignKey('hocky.id_hocky'), nullable=False)

    def __str__(self):
        return self.TenMH
class MonHoc_LopHoc(db.Model):
    __tablename__ = 'monhoc_lophoc'  # Đặt tên chính xác của bảng
    ID_lophoc = Column(Integer, ForeignKey('lophoc.ID_lophoc'), nullable=True, primary_key=True)
    IDMonHoc = Column(Integer, ForeignKey('monhoc.IDMonHoc'), nullable=True, primary_key=True)
    ID_hocky = Column(Integer, ForeignKey('hocky.id_hocky'), nullable=False)

class HocKy (db.Model):
    __tablename__ = 'hocky'
    id_hocky = Column(Integer,primary_key=True, nullable=False,autoincrement=True)
    tenHK = Column(String(50), nullable =False)
    namHoc = Column(Integer, nullable=False, default=datetime.now().year)

    def __str__(self):
        return f"{self.id_hocky} - {self.tenHK}"
class DiemSo (db.Model):
    __tablename__ = 'diemso'
    id = Column(Integer, primary_key=True, autoincrement=True)
    loaiDiem = Column (Integer , nullable =False)
    id_monhoc = Column(Integer, ForeignKey(MonHoc.IDMonHoc), nullable=False)
    id_hocky = Column(Integer,ForeignKey(HocKy.id_hocky), nullable = False)
    id_diemthanhphan = relationship("DiemThanhPhan", backref ="DiemSo",lazy = True)
    def __str__(self):
        if self.loaiDiem == 1:
            return self.id_monhoc +  "Diem Mieng"
        if self.loaiDiem == 2:
            return self.id_monhoc + "Diem 15p"
        if self.loaiDiem == 3:
            return self.id_monhoc + "Diem 45p"
        if self.loaiDiem == 4:
            return self.id_monhoc + "Diem giua ki"
        if self.loaiDiem == 5:
            return self.id_monhoc + "Diem cuoi ki"
        return "Loai ddiem khong ton tai"

class DiemThanhPhan(db.Model):
    __tablename__ ="diemthanhphan"
    id = Column(Integer, primary_key=True, autoincrement=True)
    idDiem = Column(Integer,ForeignKey(DiemSo.id),nullable = False)
    idHS = Column(Integer,ForeignKey(Student.id),nullable =False)
    idMon = Column(Integer,ForeignKey(MonHoc.IDMonHoc),nullable = False)
    giaTri = Column(Float, nullable=False)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        u1 = User(name="Admin", username="admin", password="admin_password", user_role=UserRole.quantri)
        db.session.add(u1)
        db.session.commit()



