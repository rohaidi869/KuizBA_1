def penjana_prompt_kuiz_interaktif():
    print("🚀 PENJANA PROMPT KUIZ HTML INTERAKTIF 🚀")
    print("Sila isi maklumat berikut untuk menjana kuiz interaktif:\n")
    
    # Input pengguna
    topik = input("1. Topik kuiz (cth: Teknologi Maklumat, Sejarah Islam): ").strip()
    jumlah_soalan = input("2. Bilangan soalan [default: 10]: ").strip() or "10"
    bahasa = input("3. Bahasa antaramuka (AR/BM/BI) [AR]: ").strip().upper() or "AR"
    pelajaran = input("4. Nama pelajaran/subjek [default: sama seperti topik]: ").strip() or topik
    
    # Peta kod bahasa
    bahasa_map = {
        "AR": "Arab",
        "BM": "Bahasa Melayu",
        "BI": "Bahasa Inggeris"
    }
    
    # Menjana prompt akhir
    prompt = f"""
Anda adalah seorang pakar dalam mencipta kuiz interaktif berdasarkan topik bagi pelajaran yang diberikan. Tugasan anda adalah untuk menghasilkan kod HTML lengkap untuk kuiz interaktif. 

**Spesifikasi:**
- Topik: {topik}
- Pelajaran: {pelajaran}
- Bahasa: {bahasa_map[bahasa]}
- Soalan: {jumlah_soalan}
- Format: Pilihan berganda (4 pilihan)

**Struktur Wajib:**
1. HTML lengkap dengan CSS+JS
2. 3 Halaman: Start, Kuiz, Sijil
3. Fungsi JavaScript:
   - quizData = array objek soalan
   - startQuiz(), loadQuestion(), checkAnswer()
   - navigasi soalan (sebelum/seterus)
   - sistem gred automatik

**Contoh quizData:**
```javascript
const quizData = [
  {{
    question: "Contoh soalan dalam {bahasa_map[bahasa]}?",
    options: ["Pilihan 1", "Pilihan 2", "Pilihan 3", "Pilihan 4"],
    answer: "Pilihan 3",
    explanation: "Penjelasan jawapan..."
  }},
  // ...{int(jumlah_soalan)-1} soalan lain
];
