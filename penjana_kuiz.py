def penjana_prompt_kuiz_interaktif():
    print("🚀 PENJANA PROMPT KUIZ HTML INTERAKTIF 🚀")
    print("Sila isi maklumat berikut untuk menjana kuiz interaktif:\n")
    
    # Input pengguna
    topik = input("1. Topik kuiz (cth: Teknologi Maklumat, Sejarah Islam): ").strip()
    
    # Penanganan kesilapan untuk bilangan soalan
    jumlah_soalan = "10"
    while True:
        try:
            input_soalan = input("2. Bilangan soalan [default: 10]: ").strip()
            if input_soalan == "":
                break
            jumlah_soalan = str(int(input_soalan))
            if int(jumlah_soalan) < 1:
                raise ValueError
            break
        except ValueError:
            print("Sila masukkan nombor yang sah (minima 1 soalan)")
    
    # Penanganan kesilapan untuk bahasa
    bahasa_map = {"AR": "Arab", "BM": "Bahasa Melayu", "BI": "Bahasa Inggeris"}
    bahasa = "AR"
    while True:
        input_bahasa = input("3. Bahasa antaramuka (AR/BM/BI) [AR]: ").strip().upper()
        if input_bahasa == "":
            break
        if input_bahasa in bahasa_map:
            bahasa = input_bahasa
            break
        print("Pilihan tidak sah. Sila masukkan AR, BM, atau BI.")
    
    pelajaran = input("4. Nama pelajaran/subjek [default: sama seperti topik]: ").strip() or topik
    
    # Menjana prompt akhir dengan format yang betul
    prompt = f"""
Anda adalah seorang pakar dalam mencipta kuiz interaktif berdasarkan topik bagi pelajaran yang diberikan. Tugasan anda adalah untuk menghasilkan kod HTML lengkap untuk kuiz interaktif. 

**Spesifikasi:**
- Topik: {topik}
- Pelajaran: {pelajaran}
- Bahasa: {bahasa_map[bahasa]}
- Soalan: {jumlah_soalan}
- Format: Pilihan berganda (4 pilihan)

**Struktur Wajib:**
1. HTML lengkap dengan CSS dan JavaScript
2. Tiga halaman:
   - Halaman Mula (input nama)
   - Halaman Kuiz (soalan & jawapan)
   - Halaman Sijil (paparan gred)
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
