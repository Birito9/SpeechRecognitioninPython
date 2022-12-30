import os
import random
import time
import mysql.connector
import playsound
import speech_recognition as sr
from gtts import gTTS



def main():
    def condb():
        db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='dacn')
        return db

    def speak(text):
        r1 = random.randint(1, 10000000)
        r2 = random.randint(1, 10000000)
        randfile = str(r2) + "randomtext" + str(r1) + ".mp3"
        print("Trợ lý: {}".format(text))
        tts = gTTS(text=text, lang='vi', slow=False)
        tts.save(randfile)
        playsound.playsound(randfile)
        os.remove(randfile)

    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Trợ Lý: Đang Nghe", end='\nTôi: ')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio, language="vi-VN")
                print(text)
                return text
            except:
                print("...")
                return 0

    def stop():
        speak("Hẹn gặp lại bạn sau!")

    def get_text():
        for i in range(3):
            text = get_audio()
            if text:
                return text.lower()
            elif i < 2:
                speak("Bot không nghe rõ. Bạn nói lại được không!")
        time.sleep(2)
        stop()
        return 0

    def searchsinhvien(MaSV):
        try:
            db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='dacn')
            cursor = db.cursor()
            sql = "select * from sinhvien where MaSV = '"+ MaSV +"';"
            cursor.execute(sql)
            row = cursor.fetchone()
            row_2 = '| {:<10} | {:<20} | {:<10} | {:<5} | {:<10} | {:<15} | {:<25} | {:<10} | ' \
                    '{:<10} |'.format('MaSV', 'HoSV', 'TenSV', 'Phai', 'NgaySinh', 'NoiSinh', 'Nganh', 'HeDaoTao', 'NamNhapHoc')
            print(row_2)
            print('| {:<10} | {:<20} | {:<10} | {:<5} | {:<10} | {:<15} | {:<25} | {:<10} | '
                  '{:<10} |'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        finally:
            db.close()

    def AddSinhVien(MaSV, HoSV, TenSV, Phai, NgaySinh, NoiSinh, Nganh, HeDaoTao, NamNhapHoc):
        try:
            db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='dacn')
            cursor = db.cursor()
            sql = "INSERT INTO sinhvien (MaSV, HoSV, TenSV, Phai, NgaySinh, NoiSinh, Nganh, HeDaoTao, NamNhapHoc) VALUES ('" + MaSV + "',  '" + HoSV + "', '" + TenSV + "', '" + Phai + "', '" + NgaySinh + "', '" + NoiSinh + "', '" + Nganh + "', '" + HeDaoTao + "', '" + NamNhapHoc + "');"
            cursor.execute(sql)
            db.commit()
        finally:
            db.close()

    def UpdateSinhVien(MaSV, HoSV, TenSV, Phai, NgaySinh, NoiSinh, Nganh, HeDaoTao, NamNhapHoc):
        try:
            db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='dacn')
            cursor = db.cursor()
            sql = "UPDATE SINHVIEN SET HoSV = '"+ HoSV +"', TenSV = '"+ TenSV +"' , Phai = '"+ Phai +"', NgaySinh = '"+ NgaySinh +"', NoiSinh = '"+ NoiSinh +"', Nganh = '"+ Nganh +"', HeDaoTao = '"+ HeDaoTao +"', NamNhapHoc = '"+ NamNhapHoc +"'  WHERE MaSV = '"+ MaSV +"';"
            cursor.execute(sql)
            db.commit()
        finally:
            db.close()

    def DelSinhVien(MaSV):
        try:
            db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='dacn')
            cursor = db.cursor()
            sql = "DELETE From SINHVIEN WHERE MaSV = '"+ MaSV +"';"
            cursor.execute(sql)
            db.commit()
        finally:
            db.close()

    speak("Chào mừng đến với Trường đại học Công Nghệ Sài Gòn, có thể cho tôi biết bạn là quản trị viên hay sinh viên được không")
    while True:
        # text = get_text()
        text = "quản trị viên"
        if not text:
            break
        if "dừng" in text or "tạm biệt" in text or "tắt" in text or "ngủ thôi" in text or "dừng lại" in text or "dừng chương trình" in text:
            stop()
            break
        elif "quản trị viên" in text:
            speak("bạn cần thêm, xóa hay cập nhật dữ liệu")
            # text = get_audio()
            text = "thêm"
            if "Thêm" in text or "thêm" in text:
                MaSV = input("Nhập Mã Sinh Viên của sinh viên: ").upper()
                speak("Họ của sinh viên là: ")
                HoSV = get_text().title()
                speak("Tên của sinh viên là: ")
                TenSV = get_text().title()
                speak("Giới tính của sinh viên là: ")
                Phai = get_text().title()
                speak("Nơi sinh của sinh viên là: ")
                NoiSinh = get_text().title()
                speak("Ngành của sinh viên là: ")
                Nganh = get_text().title()
                speak("Hệ Đào Tạo của sinh viên là: ")
                HeDaoTao = get_text().title()
                NgaySinh = input("Nhập ngày sinh của sinh viên: ")
                NamNhapHoc = input("Nhập Năm Nhập Học của sinh viên: ")
                speak("Thông tin sinh viên đã nhập là "+MaSV+" "+HoSV+" "+TenSV+" "+Phai+" "+NgaySinh+" "+NoiSinh+" "+Nganh+" "+HeDaoTao+" "+NamNhapHoc+"")
                AddSinhVien(MaSV, HoSV, TenSV, Phai, NgaySinh, NoiSinh, Nganh, HeDaoTao, NamNhapHoc)
            elif "Xóa" in text or "xóa" in text:
                MaSV = input("Nhập Mã Sinh Viên của bạn muốn xóa: ")
                DelSinhVien(MaSV)
            elif "Cập Nhật" in text or "cập nhật" in text:
                MaSV = input("Nhập Mã Sinh Viên của bạn muốn sửa: ").upper()
                speak("Họ của sinh viên là: ")
                HoSV = get_text().title()
                speak("Tên của sinh viên là: ")
                TenSV = get_text().title()
                speak("Giới tính của sinh viên là: ")
                Phai = get_text().title()
                speak("Nơi sinh của sinh viên là: ")
                NoiSinh = get_text().title()
                speak("Ngành của sinh viên là: ")
                Nganh = get_text().title()
                speak("Hệ Đào Tạo của sinh viên là: ")
                HeDaoTao = get_text().title()
                NgaySinh = input("Nhập ngày sinh của sinh viên: ")
                NamNhapHoc = input("Nhập Năm Nhập Học của sinh viên: ")
                speak("Thông tin sinh viên là " + MaSV + " " + HoSV + " " + TenSV + " " + Phai + " " + NgaySinh + " " + NoiSinh + " " + Nganh + " "
                      + HeDaoTao + " " + NamNhapHoc)
                UpdateSinhVien(MaSV, HoSV, TenSV, Phai, NgaySinh, NoiSinh, Nganh, HeDaoTao, NamNhapHoc)
            else:
                speak("hiện tại chưa có chức năng bạn yêu cầu, xin hãy nói lại.")
        elif "sinh viên" in text:
            speak("Có thể cho tôi biết thông tin về bạn được không.")
            speak("Tên bạn là gì ")
            TenSV = get_text().capitalize()
            speak("Chào bạn {}".format(TenSV))
            speak("bạn {}".format(TenSV) + " Hãy nhập mã sinh viên để tôi tìm kiếm.")
            MaSV = input("Nhập Mã Sinh Viên của bạn: ").upper()
            searchsinhvien(MaSV)
            time.sleep(2)
            speak("Bạn có cần hỏi gì không?.")
            while True:
                text = get_text()
                if not text:
                    break
                if "dừng" in text or "tạm biệt" in text or "tắt" in text or "ngủ thôi" in text or "dừng lại" in text or "dừng chương trình" in text:
                    stop()
                    break
                if "ngày học" in text:
                    speak("Ngày mai.")
                elif "một chỉ" in text or "bao nhiêu tiền" in text or "một chỉ bao nhiêu tiền" in text:
                    speak("Lý thuyết: 613.000 đồng 1 chỉ, Thực hành 613.000 đồng 1 chỉ")
                elif "một tiết học bao nhiêu phút" in text or "một tiết học" in text or "một tiết học bao nhiêu" in text:
                    speak("Một tiết học có 45 phút")
                elif "giới thiệu" in text:
                    speak("Trong thời đại 4.0, số lượng người được tiếp cận công nghệ rất lớn đặc biệt là công nghệ AI trợ lý ảo, chính vì thế hàng loạt các phần mềm AI trợ lý ảo được ra mắt liên tục để phục vụ con người. "
                          "Ứng dụng tư vấn tuyển sinh bằng trợ lý ảo chạy trên nền tảng máy tính, vì chạy online nên yêu cầu thiết bị phải kết nối Internet."
                          "Ứng dụng sẽ trả lời những câu hỏi được chèn sẵn giúp người dùng có thể tra cứu những thông tin về tư vấn tuyển sinh, ứng dụng sẽ trả lời người dùng nhanh nhất có thể."
                          "Chúng em chọn Python và MySQL (là một nền tảng của công nghệ AI đã và đang phát triển) để lập trình ra hệ thống tuyển sinh. "
                          "Và ngoài ra người điều hành cũng có thể chỉnh sữa database ngay trên hệ thống mà không cần vào MySQL thông qua những chức năng có sẵn trên phần mềm.")
                elif "mấy ngành" in text or "trường có bao nhiêu ngành học" in text or "trường có mấy lĩnh vực" in text:
                    speak("Trường có 3 lĩnh vực là:"
                          "1 Lĩnh vực thiết kế, mỹ thuật, nghệ thuật gồm ngành: thiết kế công nghiệp"
                          "2 Lĩnh vực Kinh tế, quản lý gồm ngành quản trị kinh doanh"
                          "3 Lĩnh vực Kỹ thuật, công nghệ gồm ngành: Công nghệ kỹ thuật Cơ điện tử, Công nghệ kỹ thuật điện điện tử, công nghệ kỹ thuật điện tử viễn thông, công nghệ thông tin, công nghệ thực phẩm và kỹ thuật xây dựng")
                elif "ngành công nghệ thông tin lấy bao nhiêu điểm" in text or "điểm công nghệ" in text:
                    speak("Năm 2022 Trường đại học Công Nghệ Sài Gòn lấy:"
                          ",Điểm thi THPT: 21.5 điểm"
                          ",Điểm xét học bạ: 21 diểm"
                          ",Điểm Đánh giá năng lực: 700 điểm")
                elif "trường có bao nhiêu cơ sở" in text or "cơ sở" in text:
                    speak("Hiện này trường chỉ có 1 cơ sở ở địa chỉ"
                          "180 Cao Lỗ, Phường 4, Quận 08, TP. Hồ Chí Minh")
                elif "học công nghệ có cần giỏi toán không" in text or "cần giỏi toán không" in text:
                    speak("Ngành công nghệ thông tin là ngành học khá “khó nhằn” bởi nó bao gồm những kiến thức lập trình phức tạp. "
"Vậy nên rất nhiều bạn thắc mắc học IT có khó không và học công nghệ thông tin có cần giỏi toán không? "
                          "Câu trả lời ở đây là, học công nghệ thông tin cũng cần có năng khiếu và những kiến thức về toán học. "
                          "Tuy nhiên, không phải học giỏi toán thì mới có thể theo học CNTT."
                          "Giỏi toán là một trong những lợi thế để bạn học những kiến thức, kỹ năng cơ bản. "
                          "Kiến thức tư duy toán học, logic thuật toán tốt sẽ hỗ trợ hiệu quả cho sinh viên trong việc học những môn học liên quan khi học chuyên ngành CNTT.")
                elif "hệ đào tạo" in text:
                    speak("Hiện nay trường gồm hệ đạo tạo chính quy là đại học và cao đẳng")
                elif "Học công nghệ thông tin có khó không" in text or "có vất vả không" in text:
                    speak("Công nghệ thông tin có khó không là nỗi lo của rất nhiều bạn trẻ khi đứng giữa nhiều lựa chọn trên con đường sự nghiệp tương lai. "
                          "Dù là ngành học hấp dẫn nhưng Công nghệ thông tin không phải là ngành có thể “đua đòi” chạy theo “mốt”. "
                          "Công nghệ thông tin là ngành thay đổi và cập nhật từng giờ. "
                          "Vì vậy, lượng kiến thức trong sách vở, giáo trình mà bạn học chắc chắn không bao giờ là đủ. "
                          "Để thành thạo trong lĩnh vực này, bạn cần không ngừng bồi dưỡng kiến thức, cập nhất và tham khảo các xu hướng công nghệ thông tin hiện nay. "
                          "Nếu học tập theo đúng chương trình, biết mở rộng những vấn đề đã học cũng như chăm chỉ tìm kiếm những kiến thức mới, bạn sẽ có hành trang vững chắc để bước vào thị trường việc làm. "
                          "Ngược lại, nếu thụ động và chỉ học qua môn để có tấm bằng tốt nghiệp thì chắc chắn, bạn sẽ gặp nhiều vất vả khi làm các dự án sau này. "
                          "Có thể thấy, việc học Công nghệ thông tin có khó không còn phụ thuộc vào khả năng và nỗ lực của chính bạn. "
                          "Bên cạnh đó, sinh viên còn cần chọn một môi trường có lộ trình đào tạo và định hướng lâu dài để phát triển. "
                          "Như vậy bạn mới có cơ hội để tiếp cận và cọ xát với những dự án thực tế. ")
                elif "thời gian một học kỳ là bao lâu" in text or "thời gian 1 học kỳ là bao lâu" in text or "thời gian một học kỳ" in text:
                    speak("Thời gian 1 học kỳ là 3 tháng nhé!")
                speak("Bạn còn câu hỏi nào nữa không?.")
        else:
            speak("Bot không nghe rõ. Bạn nói lại được không!")

        def disdb():
            condb().close()
main()