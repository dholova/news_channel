class PostDB:
    storage = [
        {
            'id': 1,
            'title': 'Хакери з групи Conti, які можуть бути пов’язані з рф, атакували об’єкти критичної інфраструктури України',
            'text': '''
            Група кіберзлочинців, яка складається з колишніх учасників банди вимагачів Conti, тепер задіяна не лише у фінансових махінаціях, а й у політичних. DOU дізнався, як саме з квітня 2022-го ці хакери близько десяти разів атакували об’єкти критичної інфраструктури України.
            '''

        },
        {
            'id': 2,
            'title': 'Міноборони відтермінувало обов’язковий військовий облік жінок на рік',
            'text': '''
            Міноборони підготувало наказ, яким вчергове відтермінувало строки взяття жінок низки професій/спеціальностей на військовий облік ще на рік — до 1 жовтня 2023 року. Документ 6 вересня підписав міністр оборони Олексій Резніков.
            Також наразі в парламенті доопрацьовується проєкт Закону, який має врегулювати питання військового обліку жінок і зробити його виключно добровільним, навіть під час воєнного стану.            
            '''
        },
        {
            'id': 3,
            'title': '1Xbet позбавили ліцензії в Україні',
            'text': '''
            Російську гральну мафію 1Xbet позбавили ліцензії в Україні. Тепер  росіяни не зможуть збирати особисті дані українців, які є в групі ризику на вербування через цей механізм гральної залежності. Про це повідомили в телеграм-каналі InformNapalm.
            '''
        }
    ]
    last_id = 3
    def get_all(self):
        return self.storage

    def get_one(self, id_):
        for post in self.storage:
            if post['id'] == id_:
                return post

    def create(self, title, text):
        self.last_id +=1
        new_post = {
            'id': self.last_id,
            'title': title,
            'text': text
        }
        self.storage.append(new_post)
        return new_post
    def update(self, id_, title, text):
        post = {
            'id': id_,
            'title': title,
            'text': text
        }
        for i in range(len(self.storage)):
            if self.storage[i].get('id') == id_:
                self.storage[i] = post

        return post
    def delete(self, id_):
        self.storage = [post for post in self.storage if post['id'] != id_]