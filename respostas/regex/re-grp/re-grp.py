import re
import datetime

meu_aniversario = datetime.date(2000,2,2)

# Gerada pelo arquivo reg-rp-q1.py
## RESPOSTA: 1977-05-13

entrada = """
Eligendi impedit sit quod sunt. Voluptate at perferendis culpa saepe. Optio consequuntur temporibus molestiae iure ea. Eveniet consequuntur veniam non eaque. Numquam quis beatae ullam molestiae. Iusto cumque occaecati necessitatibus quas odit 1398-07-12 numquam. Eaque voluptates itaque explicabo incidunt. Alias suscipit cumque sequi expedita corrupti similique consectetur. Animi consequatur adipisci. Excepturi officiis voluptate dolores exercitationem sed. Voluptatem nihil earum facilis illum commodi a. Veniam fuga doloribus quia consectetur dolores. Praesentium fugiat aliquam repellat.

Debitis reiciendis 1442-09-14 vitae beatae ex. Ducimus ex praesentium maiores officiis. Earum perspiciatis eius incidunt. Quas cum aspernatur placeat quasi non. Veniam accusamus quaerat consectetur nihil officiis cumque. Dolore enim commodi vel fuga at fugit reprehenderit. Modi eligendi perspiciatis dolorem. Et amet nihil eligendi velit. Natus qui nulla tempora molestiae quam.

Pariatur quam adipisci minus sapiente cupiditate dolores. Voluptatem vel minus. Illum doloremque porro magni est natus blanditiis sapiente. Nulla 1058-02-12T12:52+19:30 temporibus quisquam amet reprehenderit velit. Quia veritatis porro necessitatibus nobis. Ipsam repellat incidunt. Voluptatum consectetur incidunt ipsam sed. Est ad tempore adipisci necessitatibus doloribus. Sed voluptates facere enim. Nobis est repudiandae laborum 1058-02-12T12:52+19:30 nobis.

Nisi laborum veritatis ea suscipit. Reprehenderit distinctio nemo ullam vitae mollitia vitae. Fuga esse excepturi. Doloribus iusto possimus aspernatur maiores similique. Eligendi cupiditate quisquam culpa. Cum quidem odio laboriosam soluta necessitatibus saepe voluptatem. Explicabo officia doloremque cupiditate veniam 1787-12-30. Unde aliquam enim. Inventore provident nobis exercitationem itaque quidem. Natus cumque eius ipsam quibusdam. Illum ab aspernatur. Qui eligendi dolores natus enim inventore.

Porro blanditiis deleniti facere odit a neque. Eligendi odit quia modi voluptas. Autem 1270-12-30 quos nobis l1315-09-16oriosam repellendus nobis. Iure in praesentium officia praesentium in optio. Unde accusamus ea rem numquam excepturi. Ex sit alias nihil mollitia quis. Quod fuga sed 1315-09-16 similique 1861-03-15T22:45 nam. Inventore nemo ducimus l1315-09-16orum vero occaecati distinctio. Possimus error facere.

1574-04-20T17:45 voluptatibus suscipit 1084-07-27 quos pariatur. Ad ratione itaque dolorum saepe ullam. Fuga rerum odio 1084-07-27. Dolores delectus illum veniam perferendis. Inventore facilis ullam ipsam reiciendis possimus maiores. Facere quam nisi consequuntur unde quisquam fugiat. Debitis deleniti sapiente.

Dolore voluptas nulla at dolorum reprehenderit dignissimos. Corrupti iste odit odio. Aut autem numquam quos eaque quis. Reiciendis asperiores hic exercitationem soluta. Ab quasi aliquam. Veritatis perspiciatis eaque 1577-06-31. Beatae velit aspernatur modi quaerat magni quae. Quasi recusandae in doloribus perspiciatis quae unde.

1977-05-13 nesciunt cupiditate inventore laboriosam tempore. Iusto nulla officia eligendi illum. Nostrum quia adipisci a commodi ipsum. Itaque molestias voluptatum voluptate. Sapiente debitis repudiandae similique eligendi natus quia. Id illo optio dolorem. Corporis quidem quibusdam. Totam provident fugit aperiam. Perspiciatis laborum aliquam voluptas qui similique. Reprehenderit eveniet animi culpa. Cupiditate esse quaerat est saepe doloribus iusto. Maxime totam ut aspernatur quam omnis aliquid. Perferendis nobis a at corporis repellat ipsam sapiente.

Dolore itaque 1251-07-14T14:33+22:00 error. Soluta 1134-01-25 quis asperiores. Aspernatur possimus ad qui iusto quasi. Quisquam fugiat ipsum recusandae adipisci. Laudantium necessitatibus enim culpa laudantium dolore tenetur optio. Quasi provident laudantium doloribus esse recusandae fuga natus. Atque iusto 1134-01-25 aspernatur voluptates.

Nemo quasi nulla. Dolorem ad ipsum quas voluptatem. Provident dolorem possimus omnis. Repellendus harum eos illum hic provident. Dicta doloribus mollitia quisquam reprehenderit rem consequuntur rem. Officia 1167-11-21T22:22 aut minima. Corporis fugit accusamus nisi. Non dolorum mollitia animi. Eum placeat commodi facilis repellat iste. 1076-04-21T12:04 incidunt ullam. Id et nesciunt sequi. Ratione dolores accusamus magnam at.
"""

regex = re.compile(r"(?P<year>\d{4})-(?P<month>\d\d)-(?P<day>\d\d)(?P<time>T\d\d:\d\d:\d\d)?(?P<timeZone>\d:\d)?")

datas = []
subtraida = []

for data in regex.finditer(entrada):
    try:
        datas.append(datetime.date(int(data.groupdict()['year']), int(data.groupdict()['month']), int(data.groupdict()['day'])))
    except ValueError:
        continue

for data in datas:
    subtraida.append(abs(meu_aniversario - data))

print("A minha data de nascimento é:", meu_aniversario)
print("A data econtrada mais próxima da minha data de nascimento é:", datas[subtraida.index(min(subtraida))])