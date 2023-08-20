Реализация трекера полезных привычек с использованием ТГ

В проекте к стандартной моделе Юзера добавляется id чата тг, для получения сообщений от программы.

Работа программы:
1) Регистрируем юзера через token
2) После регистрации можно создавать привычки
3) При создании привычки отправляется сообщение в ТГ о создании,

а напоминание происходит через celery(chek_habit в tasks.py)

Модель Habit:

Пользователь — создатель привычки.
Место — место, в котором необходимо выполнять привычку.
Время — время, когда необходимо выполнять привычку.
Действие — действие, которое представляет из себя привычка.
Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.