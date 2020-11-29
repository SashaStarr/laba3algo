# laba3algo
Код задачi: CAREER
Ви хочете зробити кар’єру у великiй корпорацiї, яка має складну iєрархiчну структуру
та багато посад. Проте, читаючи вiдгуки працiвникiв на GlassDoor, ви дiзнаєтеся,
що рiзнi посади в цiй компанiї приносять зовсiм рiзну кiлькiсть корисного досвiду,
тому є сенс ретельно обирати, на яких посадах ви хочете працювати.
Органiзацiйна структура компанiї має форму пiрамiди, де вищий рiвень має рiвно
на 1 посаду менше, нiж нижчий. Досвiд, який можна здобути на кожнiй посадi, а
також способи пiдвищення вказанi на схемi:

4

3 1

2 1 5

1 3 2 1

Працiвник може бути переведений тiльки на вищу посаду (з вищої на нижчу рухатись
не дозволяється).
Знаючи досвiд, який можна здобути на кожнiй посадi в компанiї, визначте максимальну
суму досвiду, яку ви можете здобути, почавши працювати на найнижчому рiвнi.

# Вхiднi данi

Вхiдний файл career .in складається з L + 1 рядкiв.
• Перший рядок мiстить L — кiлькiсть органiзацiйних рiвнiв в компанiї.
1 ≤ L ≤ 1000
• Наступнi L рядкiв мiстять 1, 2, 3, ..., L−2, L−1, L натуральних чисел E — досвiд
для кожної посади на даному рiвнi.
0 ≤ E < 10000

# Приклад 
career .in
4
4
3 1
2 1 5
1 3 2 1
career .out
12
