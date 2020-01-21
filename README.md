# oblakogroupqa
Для запуск теста выплнить:
1 выполнить docker run -p 80:80 -t oblakogroupqa --name kototest
2 docker exec -i -t kototest bash
3 cd features/steps/
4 behave -i test.feature