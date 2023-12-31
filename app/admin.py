from app.models import Student, User, MonHoc, LopHoc, DiemSo,MonHoc_LopHoc,  DiemThanhPhan, UserRole,HocKy
from app import admin, db
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose,AdminIndexView,Admin
from flask_login import logout_user, current_user
from flask import redirect
from datetime import datetime
from flask import Flask, flash, redirect, url_for, render_template
from flask_admin import form, expose



class StudentAdmin(ModelView):
    def on_model_change(self, form, model, is_created):
        # Kiểm tra điều kiện về độ tuổi (15 - 20)
        if model.ngaysinh:
            today = datetime.now().date()
            age = today.year - model.ngaysinh.year - (
                    (today.month, today.day) < (model.ngaysinh.month, model.ngaysinh.day))
            if not (15 <= age <= 20):
                raise ValueError("Độ tuổi của học sinh phải từ 15 đến 20.")





class StudentView(StudentAdmin):
    can_view_details = True
    edit_modal = True
    details_modal = True
    column_list = ('id','ten', 'ngaysinh', 'gioitinh', 'lophoc_id')
    form_columns = ('ten', 'ngaysinh', 'gioitinh', 'email', 'diachi', 'lophoc_id')
    column_searchable_list = ['ten']
    column_filters = ['ten']
    can_export = True
    column_exclude_list = ['image']
class SubjectView(ModelView):
    column_list = ('IDMonHoc', 'TenMH', 'id_hocky')
    form_columns = ( 'TenMH', 'id_hocky')
class UserView(ModelView):
    column_list = ('id', 'name', 'username', 'password', 'active', 'joined_date', 'user_role')

class HocKyView(ModelView):
    column_list = ('id_hocky', 'tenHK', 'namHoc')
class LopHocView(ModelView):
    column_list = ('TenLop','ID_lophoc', 'hocsinhs')

class MonHoc_LopHocView (ModelView) :
    form_columns = ('ID_lophoc', 'IDMonHoc','ID_hocky')
    column_list = ('ID_lophoc', 'IDMonHoc','ID_hocky','monhocs')
class diemthanhphanView(ModelView):
    pass
class DiemtongView(ModelView):
    form_columns = ('loaiDiem', 'id_monhoc', 'id_hocky')
    column_list = ('id', 'loaiDiem', 'id_monhoc', 'id_hocky','id_diemthanhphan')
class diemthanhphanView(ModelView):
    form_columns = ('idDiem', 'idHS', 'idMon','giaTri')
    column_list = ('id','idDiem', 'idHS', 'idMon','giaTri')



admin.add_view(StudentView(Student, db.session, name='Tiếp nhận học sinh'))
admin.add_view(SubjectView(MonHoc, db.session, name='Quản lý môn học'))
admin.add_view(LopHocView(LopHoc, db.session, name='LopHoc'))

admin.add_view(DiemtongView(DiemSo, db.session, name='Điểm Tổng'))
admin.add_view(diemthanhphanView(DiemThanhPhan, db.session, name='Điểm Thành Phần'))









