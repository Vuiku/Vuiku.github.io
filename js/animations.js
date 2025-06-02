// Функция для запуска анимации
function startPageAnimation() {
    // Сначала убираем класс, чтобы сбросить анимацию
    document.body.classList.remove('page-loaded');
    
    // Запускаем анимацию через небольшую задержку
    setTimeout(() => {
        document.body.classList.add('page-loaded');
    }, 10);
}

// Обработка первоначальной загрузки страницы
document.addEventListener('DOMContentLoaded', startPageAnimation);

// Обработка обновления страницы
window.addEventListener('pageshow', (event) => {
    // Проверяем, загружена ли страница из кэша
    if (event.persisted) {
        startPageAnimation();
    }
});

// Обработка перехода между страницами
document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', (e) => {
        // Пропускаем внешние ссылки
        if (link.hostname !== window.location.hostname) {
            return;
        }

        e.preventDefault();
        const target = link.href;

        // Анимация исчезновения
        document.body.classList.add('page-exit');

        // Переход на новую страницу после завершения анимации
        setTimeout(() => {
            window.location.href = target;
        }, 800); // Увеличили время до перехода, чтобы соответствовать новой длительности анимации
    });
});

// Обработка обновления страницы по F5 или Ctrl+R
document.addEventListener('keydown', (e) => {
    if (e.key === 'F5' || (e.ctrlKey && e.key === 'r')) {
        document.body.classList.add('page-exit');
    }
});

// Обработка обновления через кнопку браузера
window.onbeforeunload = function() {
    document.body.classList.add('page-exit');
}; 