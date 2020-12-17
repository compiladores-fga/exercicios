import re
import datetime
from datetime import timedelta

texto = """
Quaerat consequuntur ab laudantium ipsa. Id magnam nemo illo molestias laudantium esse. Aliquid laborum magni. Natus inventore ratione accusamus. 1574-11-27T16:52+22:00 incidunt deleniti consectetur. Architecto voluptas fugit harum. Nobis laborum harum optio eveniet. Aperiam rerum eveniet doloremque. Perspiciatis pariatur consequuntur suscipit distinctio deleniti provident. Molestias adipisci id temporibus. Consectetur distinctio 1588-09-15T01:24 a cum.

Modi officiis maxime saepe beatae. Est consequatur voluptatibus ratione sapiente officiis iste magni. Voluptas esse expedita a ullam omnis enim. Occaecati quia autem similique quas. Tempore voluptatibus possimus molestiae provident ipsa. Qui delectus culpa. Possimus consectetur facere sunt excepturi asperiores provident. Accusamus maiores reprehenderit est. Quam consequuntur molestias nostrum eligendi ipsam.

Eos ex iste veniam officia. Dolores iste numquam laborum quae magni minima. Perferendis repudiandae alias mollitia. Pariatur assumenda sit impedit praesentium. Non delectus odio praesentium eos facilis labore enim. Dolorem facere perferendis repellendus animi consequatur earum. Accusantium tempora esse doloribus. Minus delectus placeat doloremque. Eveniet enim iste minima perferendis. Quaerat natus quia dolor ut quia inventore.

Dignissimos commodi porro culpa quidem. Cum ducimus ipsa est officia magni autem quibusdam. Error aut aliquam quos ducimus aspernatur consectetur. Illo exercitationem maxime veritatis reiciendis iusto numquam. Numquam harum exercitationem amet aut similique. Suscipit aut sit temporibus. Architecto provident 1734-11-21 voluptates. Eaque iste excepturi. Suscipit 1734-11-21 quisquam accusamus.

Dolorem aut quia totam quibusdam doloremque. Quos delectus voluptates commodi corrupti. Quibusdam inventore necessitatibus voluptatibus. Ullam quibusdam fuga dignissimos distinctio. Iure culpa eligendi accusantium facilis eius ratione. Debitis impedit atque. Nesciunt inventore molestias et odio. Odio 1245-07-27 maxime eveniet. Illum blanditiis perferendis veritatis sed magni. Laudantium consectetur dolor hic. Ipsam vitae laboriosam repellendus nulla. Quae 1640-07-29 laborum veniam adipisci.

Ad nisi fuga voluptatum. Ratione maxime voluptate est. Repudiandae pariatur consequuntur odio nesciunt maxime animi corrupti. Quas qui cumque culpa repellat culpa. Officiis nam itaque delectus beatae ducimus itaque. Magnam reprehenderit aperiam mollitia 1348-02-16. Provident officiis voluptas fugiat quibusdam eos. Nostrum doloremque deserunt necessitatibus voluptatum recusandae eius veniam. Sequi vero architecto impedit. Aut commodi molestias eligendi. Vero itaque maiores ab. Pariatur non quos facilis eligendi eos.

Quo possimus laudantium ex 1233-10-12 eaque 2000-05-03T01:03+00:30. Iure expedita qui quidem quidem voluptate sit nesciunt. Nesciunt tempora laudantium 1528-03-24T24:17+06:00 aspernatur dignissimos unde. Sapiente 1528-03-24T24:17+06:00 molestias dolores m1528-03-24T24:17+06:00ima. Voluptate amet ut voluptatum unde beatae commodi. Accusamus reprehenderit cupiditate hic.

Nemo consequatur ipsum atque veritatis neque necessitatibus. Eum deleniti facilis aspernatur corporis optio. Adipisci aperiam a adipisci laborum. Voluptatem iure voluptas totam est voluptatem corporis. Molestias qui nemo voluptate consequuntur. Quae necessitatibus voluptatibus facere vitae 1864-08-18 ab.

Iusto autem ratione vero excepturi ad voluptates animi. Necessitatibus fugiat temporibus ex esse exercitationem. Dicta eius 1692-11-06 sit. Dolor fugit id quaerat voluptatum quisquam. Voluptates temporibus consequuntur dolorem consequatur qui. A ducimus dolore eligendi optio voluptate. A maxime aperiam dicta autem nostrum quas esse. Maiores esse eius illum facere assumenda. Nostrum dolorum ab accusantium assumenda ducimus sequi recusandae. Tempore quasi facilis ipsam vel voluptas. Dolorum omnis repellat 1692-11-06 debitis doloremque. Ut iste est. Eum qui eius aut facere deserunt maiores.

Voluptatem fugiat labore doloremque quae adipisci quisquam. Quo nemo hic. Perspiciatis modi eaque animi odit. Delectus dicta natus. 1174-03-03 itaque aliquid aperiam. Sint officiis repellendus iure sapiente illo. Earum adipisci debitis itaque repudiandae. Nostrum eum pariatur praesentium earum maiores accusantium. Enim repellendus dolorem mollitia occaecati. Enim sed itaque debitis.

Quasi quasi architecto odio in est ullam at. Nam maxime quos voluptates dignissimos. Velit suscipit optio. Culpa ea cum voluptatem. Deleniti aliquam voluptate quia eius ducimus. Eaque commodi nulla dicta itaque quas. Molestiae culpa aspernatur eligendi. Molestiae nobis possimus laborum. 1504-05-19 suscipit expedita ad. Nemo ab non sunt. Est neque nostrum quaerat.

Perferendis delectus similique ullam quaerat. Dolor laborum beatae. Modi 1106-08-25 nam voluptatem ab est voluptatem. Tempora odit odio. 1413-08-23T06:20 ex saepe fuga eos. Vero at illum atque. Alias facilis cupiditate error a. Ad exercitationem laborum rem esse ratione. Harum perferendis molestiae. Perferendis rerum cum id perferendis cumque. Cum eaque necessitatibus alias.

"""

meu_niver = datetime.date(2000,5,10)

r = re.compile(r"(?P<A>\d\d\d\d)-(?P<M>(0[1-9])|(1[0-2]))-(?P<D>(0[1-9])|(1[0-9])|(2[0-9])|(3[01]))(?P<H>T\d\d:\d\d:\d\d)?(?P<FH>\d:\d)?")

min_time = timedelta.max
min_niver = None
for data in r.finditer(texto):
    try:
        niver = datetime.date(int(data.groupdict()['A']), int(data.groupdict()['M']), int(data.groupdict()['D']))
        if(abs(meu_niver - niver) < min_time):
            min_niver = niver
            min_time = abs(meu_niver - niver)
    except:
        continue

print(min_niver)
