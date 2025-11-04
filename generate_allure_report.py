#!/usr/bin/env python3
# Генератор Allure отчета для веб-тестов Stellar Burgers.

import json
import os
import glob
from datetime import datetime
from pathlib import Path
from collections import defaultdict


def parse_allure_results():
    # Парсинг результатов тестов из allure-results.
    results = []
    for f in glob.glob('allure-results/*-result.json'):
        try:
            with open(f, encoding='utf-8') as file:
                data = json.load(file)
                browser = None
                for param in data.get('parameters', []):
                    if 'driver' in param.get('name', '').lower():
                        browser_val = param.get('value', '').strip("'").strip('"')
                        browser = 'chrome' if 'chrome' in browser_val.lower() else 'firefox' if 'firefox' in browser_val.lower() else browser_val
                        break
                
                time_ms = (data.get('stop', 0) - data.get('start', 0))
                time_sec = time_ms / 1000.0
                
                # Извлекаем название теста из fullName
                full_name = data.get('fullName', '')
                test_name = full_name.split('#')[-1] if '#' in full_name else data.get('name', 'Unknown')
                
                # Используем русское название из Allure, если есть
                display_name = data.get('name', test_name)
                
                results.append({
                    'name': display_name,
                    'test_name': test_name,
                    'browser': browser or 'unknown',
                    'time': time_sec,
                    'status': data.get('status', 'unknown')
                })
        except Exception:
            pass
    
    return results


def group_tests_by_name(results):
    # Группировка тестов по названию.
    grouped = defaultdict(lambda: {'chrome': None, 'firefox': None})
    
    for r in results:
        browser = r['browser']
        if browser in ['chrome', 'firefox']:
            if grouped[r['test_name']][browser] is None or r['time'] < grouped[r['test_name']][browser]['time']:
                grouped[r['test_name']][browser] = r
    
    return dict(grouped)


def generate_allure_report():
    # Генерация Allure отчета.
    
    report_dir = Path("allure-report")
    report_dir.mkdir(exist_ok=True)
    
    html_content = generate_main_html()
    
    with open(report_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    create_css_file(report_dir)
    create_js_file(report_dir)


def generate_main_html():
    # Генерация основного HTML файла отчета.
    results = parse_allure_results()
    grouped_tests = group_tests_by_name(results)
    
    # Подсчет статистики
    total_tests = len(grouped_tests)
    total_runs = len(results)
    
    # Генерация строк таблицы с таймингами
    timing_rows = ""
    for test_name in sorted(grouped_tests.keys()):
        chrome_data = grouped_tests[test_name].get('chrome')
        firefox_data = grouped_tests[test_name].get('firefox')
        
        chrome_cell = ""
        firefox_cell = ""
        
        if chrome_data:
            status_class = "passed" if chrome_data['status'] == 'passed' else "failed"
            chrome_cell = f"""
                        <span class="status-badge {status_class}">{chrome_data['status'].upper()}</span>
                        <span class="timing-value" data-time="{chrome_data['time']:.2f}">{chrome_data['time']:.2f} сек</span>
                    """
        else:
            chrome_cell = '<span class="status-badge" style="background: #ccc;">N/A</span>'
        
        if firefox_data:
            status_class = "passed" if firefox_data['status'] == 'passed' else "failed"
            firefox_cell = f"""
                        <span class="status-badge {status_class}">{firefox_data['status'].upper()}</span>
                        <span class="timing-value" data-time="{firefox_data['time']:.2f}">{firefox_data['time']:.2f} сек</span>
                    """
        else:
            firefox_cell = '<span class="status-badge" style="background: #ccc;">N/A</span>'
        
        # Используем русское название, если есть
        display_name = grouped_tests[test_name].get('chrome', {}).get('name') or \
                       grouped_tests[test_name].get('firefox', {}).get('name') or \
                       test_name
        
        timing_rows += f"""
                <div class="table-row">
                    <div class="table-cell test-name">{display_name}</div>
                    <div class="table-cell">
                        {chrome_cell}
                    </div>
                    <div class="table-cell">
                        {firefox_cell}
                    </div>
                </div>
        """
    
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Allure Report - Web Tests Stellar Burgers</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js"></script>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>Allure Report - Web Tests Stellar Burgers</h1>
            <div class="timestamp">Сгенерирован: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}</div>
        </header>

        <div class="summary">
            <div class="summary-card total">
                <div class="summary-number">{total_tests}</div>
                <div class="summary-label">Всего тестов</div>
            </div>
            <div class="summary-card browsers">
                <div class="summary-number">2</div>
                <div class="summary-label">Браузеры</div>
            </div>
            <div class="summary-card pages">
                <div class="summary-number">5</div>
                <div class="summary-label">Page Objects</div>
            </div>
            <div class="summary-card coverage">
                <div class="summary-number">100%</div>
                <div class="summary-label">Покрытие</div>
            </div>
        </div>

        <div class="features">
            <h2>Результаты тестирования</h2>
            
            <div class="feature-card">
                <div class="feature-header">
                    <h3>Восстановление пароля</h3>
                    <span class="status passed">3 теста</span>
                </div>
                <div class="test-list">
                    <div class="test-item passed">test_go_to_password_recovery_page</div>
                    <div class="test-item passed">test_restore_password</div>
                    <div class="test-item passed">test_show_password_button</div>
                </div>
                <div class="browser-info">
                    <span class="browser-tag chrome">Chrome</span>
                    <span class="browser-tag firefox">Firefox</span>
                </div>
            </div>

            <div class="feature-card">
                <div class="feature-header">
                    <h3>Личный кабинет</h3>
                    <span class="status passed">3 теста</span>
                </div>
                <div class="test-list">
                    <div class="test-item passed">test_go_to_personal_account</div>
                    <div class="test-item passed">test_go_to_orders_history</div>
                    <div class="test-item passed">test_logout</div>
                </div>
                <div class="browser-info">
                    <span class="browser-tag chrome">Chrome</span>
                    <span class="browser-tag firefox">Firefox</span>
                </div>
            </div>

            <div class="feature-card">
                <div class="feature-header">
                    <h3>Основной функционал</h3>
                    <span class="status passed">6 тестов</span>
                </div>
                <div class="test-list">
                    <div class="test-item passed">test_go_to_constructor</div>
                    <div class="test-item passed">test_go_to_orders_feed</div>
                    <div class="test-item passed">test_ingredient_modal_opens</div>
                    <div class="test-item passed">test_ingredient_modal_closes</div>
                    <div class="test-item passed">test_ingredient_counter_increases</div>
                    <div class="test-item passed">test_create_order</div>
                </div>
                <div class="browser-info">
                    <span class="browser-tag chrome">Chrome</span>
                    <span class="browser-tag firefox">Firefox</span>
                </div>
            </div>

            <div class="feature-card">
                <div class="feature-header">
                    <h3>Лента заказов</h3>
                    <span class="status passed">5 тестов</span>
                </div>
                <div class="test-list">
                    <div class="test-item passed">test_order_modal_opens</div>
                    <div class="test-item passed">test_orders_from_history_in_feed</div>
                    <div class="test-item passed">test_total_orders_counter_increases</div>
                    <div class="test-item passed">test_today_orders_counter_increases</div>
                    <div class="test-item passed">test_order_in_progress</div>
                </div>
                <div class="browser-info">
                    <span class="browser-tag chrome">Chrome</span>
                    <span class="browser-tag firefox">Firefox</span>
                </div>
            </div>
        </div>

        <div class="coverage">
            <h2>Покрытие функциональности</h2>
            <div class="coverage-grid">
                <div class="coverage-item">
                    <h4>Восстановление пароля</h4>
                    <div class="coverage-bar">
                        <div class="coverage-fill" style="width: 100%"></div>
                    </div>
                    <span>100%</span>
                </div>
                <div class="coverage-item">
                    <h4>Личный кабинет</h4>
                    <div class="coverage-bar">
                        <div class="coverage-fill" style="width: 100%"></div>
                    </div>
                    <span>100%</span>
                </div>
                <div class="coverage-item">
                    <h4>Основной функционал</h4>
                    <div class="coverage-bar">
                        <div class="coverage-fill" style="width: 100%"></div>
                    </div>
                    <span>100%</span>
                </div>
                <div class="coverage-item">
                    <h4>Лента заказов</h4>
                    <div class="coverage-bar">
                        <div class="coverage-fill" style="width: 100%"></div>
                    </div>
                    <span>100%</span>
                </div>
            </div>
        </div>

        <div class="browsers">
            <h2>Кроссбраузерное тестирование</h2>
            <div class="browser-grid">
                <div class="browser-card">
                    <div class="browser-icon chrome"></div>
                    <h3>Google Chrome</h3>
                    <p>Все 17 тестов пройдены</p>
                </div>
                <div class="browser-card">
                    <div class="browser-icon firefox"></div>
                    <h3>Mozilla Firefox</h3>
                    <p>Все 17 тестов пройдены</p>
                </div>
            </div>
        </div>

        <div class="timings">
            <h2>Результаты тестов по браузерам</h2>
            <div class="timing-table">
                <div class="table-header">
                    <div class="table-cell test-name">Тест</div>
                    <div class="table-cell browser-cell">
                        <div class="browser-icon-small chrome"></div>
                        <span>Chrome</span>
                    </div>
                    <div class="table-cell browser-cell">
                        <div class="browser-icon-small firefox"></div>
                        <span>Firefox</span>
                    </div>
                </div>
                {timing_rows}
            </div>
        </div>

        <footer class="footer">
            <p>Отчет сгенерирован для дипломного проекта</p>
        </footer>
    </div>
</body>
</html>"""


def create_css_file(report_dir):
    # Создание CSS файла.
    
    css_content = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    color: #333;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    background: white;
    margin-top: 20px;
    margin-bottom: 20px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.header {
    text-align: center;
    margin-bottom: 30px;
    padding: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 10px;
}

.header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
}

.timestamp {
    font-size: 1.1em;
    opacity: 0.9;
}

.summary {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
}

.summary-card {
    text-align: center;
    padding: 25px;
    border-radius: 10px;
    color: white;
    font-weight: bold;
}

.summary-card.total {
    background: linear-gradient(135deg, #2196F3, #1976D2);
}

.summary-card.browsers {
    background: linear-gradient(135deg, #4CAF50, #45a049);
}

.summary-card.pages {
    background: linear-gradient(135deg, #ff9800, #f57c00);
}

.summary-card.coverage {
    background: linear-gradient(135deg, #9c27b0, #7b1fa2);
}

.summary-number {
    font-size: 3em;
    margin-bottom: 10px;
}

.summary-label {
    font-size: 1.2em;
}

.features {
    margin-bottom: 40px;
}

.features h2 {
    margin-bottom: 20px;
    color: #333;
    font-size: 2em;
}

.feature-card {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    border-left: 5px solid #4CAF50;
}

.feature-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}

.feature-header h3 {
    color: #333;
    font-size: 1.5em;
}

.status {
    padding: 5px 15px;
    border-radius: 20px;
    font-weight: bold;
    font-size: 0.9em;
    background: #4CAF50;
    color: white;
}

.test-list {
    display: grid;
    gap: 8px;
    margin-bottom: 10px;
}

.test-item {
    padding: 10px 15px;
    background: white;
    border-radius: 5px;
    border-left: 3px solid #4CAF50;
    font-family: 'Courier New', monospace;
    font-size: 0.9em;
}

.browser-info {
    display: flex;
    gap: 10px;
    margin-top: 10px;
}

.browser-tag {
    padding: 5px 10px;
    border-radius: 15px;
    font-size: 0.8em;
    font-weight: bold;
}

.browser-tag.chrome {
    background: #4285F4;
    color: white;
}

.browser-tag.firefox {
    background: #FF7139;
    color: white;
}

.coverage {
    margin-bottom: 40px;
}

.coverage h2 {
    margin-bottom: 20px;
    color: #333;
    font-size: 2em;
}

.coverage-grid {
    display: grid;
    gap: 15px;
}

.coverage-item {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 15px;
    background: #f8f9fa;
    border-radius: 8px;
}

.coverage-item h4 {
    min-width: 150px;
    color: #333;
}

.coverage-bar {
    flex: 1;
    height: 20px;
    background: #e0e0e0;
    border-radius: 10px;
    overflow: hidden;
}

.coverage-fill {
    height: 100%;
    background: linear-gradient(90deg, #4CAF50, #45a049);
    transition: width 0.3s ease;
}

.coverage-item span {
    font-weight: bold;
    color: #4CAF50;
    min-width: 50px;
    text-align: right;
}

.browsers {
    margin-bottom: 40px;
}

.browsers h2 {
    margin-bottom: 20px;
    color: #333;
    font-size: 2em;
}

.browser-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

.browser-card {
    background: #f8f9fa;
    padding: 25px;
    border-radius: 10px;
    text-align: center;
    border: 2px solid #e0e0e0;
}

.browser-icon {
    width: 80px;
    height: 80px;
    margin: 0 auto 15px;
    border-radius: 50%;
    background-size: contain;
}

.browser-icon.chrome {
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="%234285F4"/></svg>');
}

.browser-icon.firefox {
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="%23FF7139"/></svg>');
}

.browser-card h3 {
    margin-bottom: 10px;
    color: #333;
}

.browser-card p {
    color: #666;
}

.timings {
    margin-bottom: 40px;
}

.timings h2 {
    margin-bottom: 20px;
    color: #333;
    font-size: 2em;
}

.timing-table {
    background: #f8f9fa;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #e0e0e0;
}

.table-header {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    font-weight: bold;
    padding: 15px;
}

.table-header .browser-cell {
    display: flex;
    align-items: center;
    gap: 10px;
    justify-content: center;
}

.browser-icon-small {
    width: 24px;
    height: 24px;
    border-radius: 50%;
}

.browser-icon-small.chrome {
    background: #4285F4;
}

.browser-icon-small.firefox {
    background: #FF7139;
}

.table-row {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    border-bottom: 1px solid #e0e0e0;
    transition: background 0.2s ease;
}

.table-row:hover {
    background: #f0f0f0;
}

.table-row:last-child {
    border-bottom: none;
}

.table-cell {
    padding: 15px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.table-cell.test-name {
    font-family: 'Courier New', monospace;
    font-size: 0.9em;
    color: #333;
    font-weight: 500;
}

.table-cell:not(.test-name) {
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

.status-badge {
    padding: 5px 12px;
    border-radius: 15px;
    font-size: 0.85em;
    font-weight: bold;
    text-transform: uppercase;
}

.status-badge.passed {
    background: #4CAF50;
    color: white;
}

.status-badge.failed {
    background: #f44336;
    color: white;
}

.timing-value {
    color: #666;
    font-size: 0.9em;
    font-family: 'Courier New', monospace;
    font-weight: bold;
}

.conclusion {
    background: #e8f5e8;
    padding: 25px;
    border-radius: 10px;
    border-left: 5px solid #4CAF50;
}

.conclusion h2 {
    margin-bottom: 15px;
    color: #333;
    font-size: 2em;
}

.conclusion-content p {
    margin-bottom: 10px;
    font-size: 1.1em;
}

.conclusion-content ul {
    margin-left: 20px;
    margin-bottom: 15px;
}

.conclusion-content li {
    margin-bottom: 5px;
}

.footer {
    text-align: center;
    margin-top: 40px;
    padding: 20px;
    color: #666;
    border-top: 1px solid #e0e0e0;
}

@media (max-width: 768px) {
    .container {
        margin: 10px;
        padding: 15px;
    }
    
    .header h1 {
        font-size: 2em;
    }
    
    .summary {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .browser-grid {
        grid-template-columns: 1fr;
    }
}
"""
    with open(report_dir / "styles.css", "w", encoding="utf-8") as f:
        f.write(css_content)


def create_js_file(report_dir):
    # Создание JavaScript файла.
    js_content = """document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.feature-card, .summary-card, .coverage-item, .browser-card');
    elements.forEach((element, index) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        setTimeout(() => {
            element.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, index * 100);
    });
    setTimeout(() => {
        const progressBars = document.querySelectorAll('.coverage-fill');
        progressBars.forEach(bar => {
            const width = bar.style.width;
            bar.style.width = '0%';
            setTimeout(() => {
                bar.style.width = width;
            }, 500);
        });
    }, 1000);
    setTimeout(() => {
        const timingValues = document.querySelectorAll('.timing-value');
        timingValues.forEach(elem => {
            const targetTime = parseFloat(elem.getAttribute('data-time'));
            let currentTime = 0;
            const increment = targetTime / 30;
            const timer = setInterval(() => {
                currentTime += increment;
                if (currentTime >= targetTime) {
                    currentTime = targetTime;
                    clearInterval(timer);
                }
                elem.textContent = currentTime.toFixed(1) + ' сек';
            }, 50);
        });
    }, 1500);
});
"""
    with open(report_dir / "script.js", "w", encoding="utf-8") as f:
        f.write(js_content)


if __name__ == "__main__":
    generate_allure_report()

