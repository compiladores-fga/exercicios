import re
import datetime

entry = """
Rem suscipit vitae provident deleniti non assumenda. At exercitationem nam in eligendi aut quae. Mollitia 1286-02-08 vitae autem. Ex saepe harum corrupti libero placeat laborum eum. Quisquam saepe at maxime laboriosam rem deserunt corrupti. Sunt odit quae eius sint 1286-02-08que unde. Praesentium labore libero inventore ullam excepturi facere. Odio harum reiciendis quaerat.

Ad rerum dignissimos ipsa consectetur nam est. Ex laborum rem pariatur nemo corporis ad. Voluptatibus quod quibusdam. Quos reiciendis voluptates. Est perspiciatis facilis nam. Labore quae sint nisi alias. Eos id unde provident necessitatibus quam. Natus sed laboriosam magni.

Quidem asperiores architecto sit sed corrupti debitis. Facere repellat laudantium ipsa maxime. Facere velit necessitatibus 1123-02-04 neque. Illum officia natus quo aspernatur recusandae blanditiis. Ratione enim doloribus omnis. Atque dolorum architecto facere. Aliquid adipisci corrupti hic autem velit quia. Inventore commodi sed ipsa praesentium consequuntur. Beatae ipsum at. Libero unde maiores corporis dolor. Exercitationem tempora ipsa nostrum sed reprehenderit facilis. Sequi blanditiis ab nobis dolor dignissimos aliquid.

Ratione dolores earum 1687-02-04T08:20+11:00. Optio vel eligendi blanditiis eveniet voluptatum impedit. Distinctio dolorum reiciendis ex iste doloremque 1945-06-13. Qui veniam dolore consectetur. Molestias laborum maxime ratione cumque quo. Similique asperiores animi porro sint. Sunt repudiandae exercitationem fuga aut ut. Eveniet quos numquam earum. At dolore esse fugiat rerum officia dolor. Expedita excepturi consequatur iste explicabo non. Tempora eius illum aliquid assumenda delectus cupiditate. Facere ab doloribus reiciendis neque 1687-02-04T08:20+11:00. Beatae amet atque minus enim.

Incidunt incidunt totam officiis at nemo. Nisi voluptatem provident error harum excepturi. Quis aliquam quod illum sit. Optio amet molestias. Accusantium natus ut quia quos. Error corrupti fuga eligendi. Pariatur cupiditate magnam quisquam illo. Fugit autem accusamus laboriosam facilis. Rem delectus eos nihil numquam. Magni porro commodi.

Magnam accusamus repellat consectetur dolore aperiam. Fugit aperiam quam. Veniam quo laboriosam commodi. Consequuntur praesentium itaque eos debitis fugiat quia iusto. Ad cum pariatur laudantium deleniti voluptates. Esse dolores placeat quam eos nemo iusto. Id omnis ex quasi omnis. Voluptate sunt eligendi harum suscipit delectus. Natus consequuntur ducimus necessitatibus eos magnam. Blanditiis perferendis beatae illo sed hic. Nostrum 1139-04-14T05:26+11:30 1177-08-09 similique doloremque assumenda quas consectetur. Placeat est magni distinctio iste assumenda facere suscipit. Nisi commodi est quam.

1026-07-14T15:07 exercitationem officia enim. Nisi autem maxime. Rerum ratione tenetur. At minima sequi. Ad facilis dolorem fugiat animi. Eligendi quas officiis sequi ipsum quidem ullam. Accusantium pariatur animi.

Mollitia porro consequuntur ratione. Id repudiandae 1674-09-06 saepe minima. Dolore molestiae labore minima. Ipsum hic non veritatis dolores numquam. Cupiditate voluptates veritatis occaecati veritatis autem. Alias iure nisi dolor. Natus repellat recusandae blanditiis. Enim aut corrupti enim natus. Repellat voluptates ab vel laboriosam eius adipisci. Qui in praesentium laboriosam in facere architecto. Doloremque sed ad cupiditate cumque.

Odio at labore 1874-03-29T14:42+02:00. Blanditiis reprehenderit veritatis autem. Sapiente quidem voluptatem unde id dolores corrupti. Praesentium assumenda at nam impedit maxime. Iste inventore quasi aliquam. Quas laborum 1538-10-23 1538-10-23 esse. Sequi sequi dolorem totam quaerat. Impedit sapiente minima ipsam. Repudiandae quasi temporibus aut sed illum. Similique provident eveniet ex sequi.

Minima qui consequatur facilis. Soluta accusamus hic eveniet minima. Vel reprehenderit tempore quia corrupti adipisci nisi animi. Possimus amet harum 1186-11-23 cupiditate. Voluptatibus quidem facilis aspernatur commodi voluptatum. Possimus explicabo natus hic et rem ducimus. Beatae voluptatem temporibus. Repellat ratione qui velit veniam esse at. Aperiam voluptas aliquam corporis incidunt mollitia laboriosam.

Soluta veniam optio laudantium quis porro. Sunt doloribus ea voluptates suscipit voluptas nemo. Aut sed aut maxime dolore ad. Eligendi quas harum voluptas nemo nulla. Debitis reiciendis id nulla iste vero totam. Maiores laudantium natus. Quaerat temporibus modi quod. Nobis corporis maiores autem rerum officia repudiandae perferendis. Adipisci quasi esse sunt esse blanditiis voluptas. Enim quasi explicabo enim ipsum commodi. Corporis placeat a nihil porro. Similique perspiciatis ratione atque id quod.
"""

my_birthday = datetime.date(1999,6,10)

regex = re.compile(r"(?P<year>\d{4})-(?P<month>\d\d)-(?P<day>\d\d)(?P<time>T\d\d:\d\d:\d\d)?(?P<timeZone>\d:\d)?")

dates_in_entry = []
#re.findall(regex, entry)

for date in regex.finditer(entry):
    dates_in_entry.append(datetime.date(int(date.groupdict()['year']), int(date.groupdict()['month']), int(date.groupdict()['day'])))

dif_dates = []
for date in dates_in_entry:
    dif_dates.append(abs(my_birthday - date))
closest_date = dates_in_entry[dif_dates.index(min(dif_dates))]

print("A data mais próxima do meu aniversário:", my_birthday, "é", closest_date)