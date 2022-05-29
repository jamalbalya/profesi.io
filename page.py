from selenium.webdriver.common.keys import Keys
from locators import MainPageLocator
import time


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def login_apps(self):
        element_input_user_name = self.driver.find_element(*MainPageLocator.USER_LOGIN)
        element_input_user_name.send_keys("recruitmentqaprofesi@yopmail.com")

        element_input_user_password = self.driver.find_element(*MainPageLocator.PASSWORD)
        element_input_user_password.send_keys("Qapr0fes1")

    def login_button(self):
        element_login = self.driver.find_element(*MainPageLocator.BUTTON_LOGIN)
        element_login.click()
        time.sleep(3)

    def create_assessment(self):
        self.driver.implicitly_wait(30)
        element_click_BUAT_ASSESSMENT = self.driver.find_element(*MainPageLocator.BUAT_ASESMEN)
        element_click_BUAT_ASSESSMENT.click()
        element_input_JUDUL_ASESMEN = self.driver.find_element(*MainPageLocator.JUDUL_ASESMEN)
        element_input_JUDUL_ASESMEN.send_keys("Assessment QA Engineer")
        element_click_TANGGAL_MULAI = self.driver.find_element(*MainPageLocator.TANGGAL_MULAI)
        element_click_TANGGAL_MULAI.click()
        element_click_START_DATE = self.driver.find_element(*MainPageLocator.START_DATE)
        element_click_START_DATE.click()
        element_click_TANGGAL_BERAKHIR = self.driver.find_element(*MainPageLocator.TANGGAL_BERAKHIR)
        element_click_TANGGAL_BERAKHIR.click()
        element_click_END_DATE = self.driver.find_element(*MainPageLocator.END_DATE)
        element_click_END_DATE.click()
        element_click_PENILAIAN_DIRI_SENDIRI = self.driver.find_element(*MainPageLocator.PENILAIAN_DIRI_SENDIRI)
        element_click_PENILAIAN_DIRI_SENDIRI.click()
        element_click_FITUR_KOMENTAR = self.driver.find_element(*MainPageLocator.FITUR_KOMENTAR)
        element_click_FITUR_KOMENTAR.click()
        element_click_SKOR_DAN_KATEGORI = self.driver.find_element(*MainPageLocator.SKOR_DAN_KATEGORI)
        element_click_SKOR_DAN_KATEGORI.click()
        element_click_DAFTAR_JABATAN = self.driver.find_element(*MainPageLocator.DAFTAR_JABATAN)
        element_click_DAFTAR_JABATAN.click()
        element_click_DAFTAR_JABATAN_DIREKTORAT_KEUANGAN = self.driver.find_element(*MainPageLocator.DAFTAR_JABATAN_DIREKTORAT_KEUANGAN)
        element_click_DAFTAR_JABATAN_DIREKTORAT_KEUANGAN.click()
        element_click_DAFTAR_JABATAN_MANAJEMEN_RESIKO_DAN_IT = self.driver.find_element(*MainPageLocator.DAFTAR_JABATAN_MANAJEMEN_RESIKO_DAN_IT)
        element_click_DAFTAR_JABATAN_MANAJEMEN_RESIKO_DAN_IT.click()
        element_click_DAFTAR_PEGAWAI_TERPILIH = self.driver.find_element(*MainPageLocator.DAFTAR_PEGAWAI_TERPILIH)
        element_click_DAFTAR_PEGAWAI_TERPILIH.click()
        element_click_ASESOR_ATASAN = self.driver.find_element(*MainPageLocator.ASESOR_ATASAN)
        element_click_ASESOR_ATASAN.click()
        element_click_ATASAN_TERPILIH = self.driver.find_element(*MainPageLocator.ATASAN_TERPILIH)
        element_click_ATASAN_TERPILIH.click()
        element_click_REKAN_KERJA = self.driver.find_element(*MainPageLocator.REKAN_KERJA)
        element_click_REKAN_KERJA.click()
        element_click_REKAN_KERJA_TERPILIH = self.driver.find_element(*MainPageLocator.REKAN_KERJA_TERPILIH)
        element_click_REKAN_KERJA_TERPILIH.click()
        element_click_BAWAHAN = self.driver.find_element(*MainPageLocator.BAWAHAN)
        element_click_BAWAHAN.click()
        element_click_BAWAHAN_TERPILIH = self.driver.find_element(*MainPageLocator.BAWAHAN_TERPILIH)
        element_click_BAWAHAN_TERPILIH.click()
        element_click_BUTTON_TAMBAH = self.driver.find_element(*MainPageLocator.BUTTON_TAMBAH)
        element_click_BUTTON_TAMBAH.click()
        element_click_BOBOT_ASESOR = self.driver.find_element(*MainPageLocator.BOBOT_ASESOR)
        element_click_BOBOT_ASESOR.click()
        time.sleep(3)
        element_click_BOBOT_DIRI_SENDIRI = self.driver.find_element(*MainPageLocator.BOBOT_DIRI_SENDIRI)
        element_click_BOBOT_DIRI_SENDIRI.click()
        time.sleep(3)
        element_click_BOBOT_DIRI_SENDIRI.send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE)
        element_click_BOBOT_DIRI_SENDIRI.send_keys(0)
        time.sleep(3)
        element_click_BOBOT_ATASAN = self.driver.find_element(*MainPageLocator.BOBOT_ATASAN)
        element_click_BOBOT_ATASAN.send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE)
        element_click_BOBOT_ATASAN.send_keys(50)
        element_click_BOBOT_REKAN_KERJA = self.driver.find_element(*MainPageLocator.BOBOT_REKAN_KERJA)
        element_click_BOBOT_REKAN_KERJA.send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE)
        element_click_BOBOT_REKAN_KERJA.send_keys(30)
        element_click_BUTTON_PUBLIKASI = self.driver.find_element(*MainPageLocator.BUTTON_PUBLIKASI)
        element_click_BUTTON_PUBLIKASI.click()
        time.sleep(3)