#Укажем что это за фича
Feature: Checking search
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: Сheck some text in search results
#И используем наши шаги.
  Given website "http://qa-assignment.oblakogroup.ru/board/:anton_timofeev#"
  Then push add new todo button
  Then select add new todo list by 'Создать новый список'
  Then add title for input 'KotoTest3'
  Then create todo list
  Then close browser