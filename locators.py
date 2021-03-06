from selenium.webdriver.common.by import By

class MainPageLocator(object):
    USER_LOGIN = (By.XPATH, "/html/body/div/div/div/div/div/div[1]/div/div/div[2]/div/div[2]/form/div[1]/div/div/input")
    PASSWORD = (By.XPATH, "/html/body/div/div/div/div/div/div[1]/div/div/div[2]/div/div[2]/form/div[2]/div/div[1]/div/div/input")
    BUTTON_LOGIN = (By.XPATH, "/html/body/div/div/div/div/div/div[1]/div/div/div[2]/div/div[2]/form/div[4]/button/div[2]")
    BUAT_ASESMEN = (By.CSS_SELECTOR, "div.vs-sidebar--item:nth-child(3)")
    JUDUL_ASESMEN = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/form/div/div[1]/div[1]/div/div/input")
    TANGGAL_MULAI = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/form/div/div[1]/div[2]/div[1]/div/div/div[1]/input")
    START_DATE = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/form/div/div[1]/div[2]/div[1]/div/div/div[2]/div/span[36]")
    TANGGAL_BERAKHIR = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/form/div/div[1]/div[2]/div[2]/div/div/div[1]/input")
    END_DATE = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/form/div/div[1]/div[2]/div[2]/div/div/div[2]/div/span[38]")
    PENILAIAN_DIRI_SENDIRI = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/form/div/div[2]/div[1]/div/div[2]/button/input")
    FITUR_KOMENTAR = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/form/div/div[2]/div[2]/div/div[1]/div[2]/button/input")
    SKOR_DAN_KATEGORI = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/form/div/div[2]/div[3]/div/div/div[2]/button/input")
    DAFTAR_JABATAN = (By.CSS_SELECTOR, ".first-node > div:nth-child(1) > span:nth-child(1)")
    DAFTAR_JABATAN_DIREKTORAT_KEUANGAN = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/form/div/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/ul/li/ul/li[2]/div/span[2]/input")
    DAFTAR_JABATAN_MANAJEMEN_RESIKO_DAN_IT = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/form/div/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/ul/li/ul/li[3]/div/span[2]/input")
    DAFTAR_PEGAWAI_TERPILIH = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/form/div/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/ul/div/div[1]/div[1]/li/div[2]/button/div[2]")
    ASESOR_ATASAN = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div[1]/header/div")
    ATASAN_TERPILIH = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div[1]/div/div/div/div[2]/ul/div/div[1]/div[1]/li/div/div[1]/div/p")
    REKAN_KERJA = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div[2]/header/div")
    REKAN_KERJA_TERPILIH = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/div/div[2]/ul/div/div[1]/div[3]/li/div/div[1]/div")
    BAWAHAN = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div[3]/header")
    BAWAHAN_TERPILIH = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div[3]/div/div/div/div[2]/ul/div/div[1]/div[2]/li/div/div[1]/div")
    BUTTON_TAMBAH = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[5]/button[2]/div[2]")
    BUTTON_PUBLIKASI = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[3]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/form/div/div[4]/button[2]/div[2]")
    BOBOT_ASESOR = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[4]/div[3]/div/div[1]/header/div")
    BOBOT_DIRI_SENDIRI = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[4]/div[3]/div/div[1]/div/div/ul/li[2]/div/div[2]/div/div/input")
    BOBOT_ATASAN = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[4]/div[3]/div/div[1]/div/div/ul/li[1]/div/div[2]/div/div/input")
    BOBOT_REKAN_KERJA = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[4]/div[3]/div/div[1]/div/div/ul/li[3]/div/div[2]/div/div/input")
    BUTTON_PUBLIKASI = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[5]/button[2]/div[2]")
