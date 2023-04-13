### 1. Основную идею эксперимента (1 параграф).
1. Размер обучаемых эмбеддингов для представления начального и последующих треков в сессии увеличен со 100 до 256.
2. В предложенной на семинаре модели, если предыдущий прослушанный пользователем трек не нашелся в базе данных, предлагается рекоммендовать случайный следующий трек.
Случайные рекоммендации для данного случая были заменены рекомендациями из топа популярных треков -- TopPop модель.
3. Была исправлена ошибка, связанная с тем, что в нейросетевой рекоммендер, предложенный на семинаре, передавался не первый трек, прослушанный пользователем в рамках текущей сессии, а предыдущий.
### 2. Детали: минимум того, что нужно знать, чтобы разобраться в реализации (1-2 параграфа + диаграмма).
Реализация рекоммендера -- botify/recommenders/contextual_updated.py. <br/>
Реализация пайплайна обучения сетки -- jupyter/NN_Training.ipynb.
### 3. Результаты A/B эксперимента - в табличке как на семинарах(1 параграф + табличка).
Прирост метрики качества -- около 48%.

![img.png](img.png)

### 4. Инструкция по запуску.
```
cd botify
docker-compose up -d --build
cd ../sim
python3 sim/run.py --episodes 5000 --config config/env.yml multi --processes 4 
cd ../botify
docker cp recommender-container:/app/log/ ../tmp/
cd ../jupyter
# Далее нужно запустить ноутбук hw1.ipynb
# P.S. Если хотите еще прогнать сетку, то ноутбук с ней лежит тут -- jupyter/NN_Training.ipynb.
```
 