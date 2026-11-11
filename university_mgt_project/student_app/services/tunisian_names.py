"""
Tunisian person names for fake data.

- Latin form: English alphabetic transliteration (ISG / official-doc style)
- Arabic form: Arabic script (stored in bio / headline for display demos)
"""

# (latin_first, latin_family, arabic_first, arabic_family, gender)
# gender: "M" | "F"
TUNISIAN_PEOPLE = [
    ("Ahmed", "Ben Ali", "أحمد", "بن علي", "M"),
    ("Mohamed", "Trabelsi", "محمد", "الطرابلسي", "M"),
    ("Youssef", "Gharbi", "يوسف", "الغربي", "M"),
    ("Sami", "Jebali", "سامي", "الجبالي", "M"),
    ("Karim", "Bouazizi", "كريم", "بوعزيزي", "M"),
    ("Hedi", "Chaabane", "هادي", "شعبان", "M"),
    ("Nabil", "Khelifi", "نبيل", "خليفي", "M"),
    ("Omar", "Mejri", "عمر", "المجري", "M"),
    ("Fares", "Hammami", "فارس", "الهمامي", "M"),
    ("Anis", "Sassi", "أنيس", "الساسي", "M"),
    ("Walid", "Dridi", "وليد", "الدريدي", "M"),
    ("Rami", "Ammar", "رامي", "عمار", "M"),
    ("Bochra", "Ben Ahmed", "بشرى", "بن أحمد", "F"),
    ("Amira", "Karray", "أميرة", "القراي", "F"),
    ("Sarra", "Mansouri", "سارة", "المنصوري", "F"),
    ("Nour", "Belhadj", "نور", "بلحاج", "F"),
    ("Ines", "Toumi", "إيناس", "التومي", "F"),
    ("Mariem", "Jlassi", "مريم", "الجلاصي", "F"),
    ("Fatma", "Riahi", "فاطمة", "الرياحي", "F"),
    ("Hiba", "Chouchane", "هبة", "الشوشان", "F"),
    ("Yasmine", "Ayari", "ياسمين", "العياري", "F"),
    ("Amina", "Sfaxi", "أمينة", "السفاكسي", "F"),
    ("Lina", "Bouzid", "لينا", "بوزيد", "F"),
    ("Salma", "Guediche", "سلمى", "القيديش", "F"),
]

TUNISIAN_CITIES = [
    ("Tunis", "تونس"),
    ("Sfax", "صفاقس"),
    ("Sousse", "سوسة"),
    ("Kairouan", "القيروان"),
    ("Bizerte", "بنزرت"),
    ("Gabes", "قابس"),
    ("Ariana", "أريانة"),
    ("Monastir", "المنستير"),
    ("Nabeul", "نابل"),
    ("Gafsa", "قفصة"),
]

DEPARTMENTS = [
    ("Computer Science", "علوم الحاسوب"),
    ("Management", "التصرف"),
    ("Finance", "المالية"),
    ("Marketing", "التسويق"),
    ("Information Systems", "نظم المعلومات"),
]

COURSE_CATALOG = [
    ("ISG-PY101", "Python Programming", "برمجة بايثون"),
    ("ISG-DJ201", "Django Web Development", "تطوير الويب بـ جانغو"),
    ("ISG-DB110", "Databases", "قواعد البيانات"),
    ("ISG-ST205", "Statistics for Business", "إحصاء للأعمال"),
    ("ISG-EN100", "English for IT", "الإنجليزية للإعلامية"),
    ("ISG-AI301", "Introduction to AI", "مقدمة في الذكاء الاصطناعي"),
]
