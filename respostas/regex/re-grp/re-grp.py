import re
import datetime

text = """
Ea delectus autem deleniti a necessitatibus. Beatae quasi repudiandae sunt. Ad asperiores officiis. Recusandae eligendi assumenda impedit dolor animi fugit nemo. Praesentium odio occaecati odit iste. Totam harum vitae error necessitatibus officiis possimus. Maiores voluptatum rerum sunt voluptates. Consequatur dicta quasi quod. Odio quidem sed possimus dolorum error aperiam nam. Velit dolore iure expedita vel eligendi. Voluptatibus corporis modi dolorem.                                                                                                                                                                                                                                      Quaerat earum pariatur qui fugiat nemo odio quam. Sint libero provident illo. Nisi reprehenderit facere beatae necessitatibus est. Consequatur quaerat nesciunt illum. Sapiente suscipit provident placeat sequi adipisci. Laborum fugit placeat nobis impedit ratione numquam. Facere praesentium fuga praesentium molestiae. Necessitatibus totam sit minima.                                                                                                                                                                                                                                                                                                                                                 Corrupti ex molestiae omnis sit fugit sit. Libero porro beatae 1325-11-20 reiciendis. Odit tenetur eius repellendus neque ex nobis nostrum. Aliquam animi fugiat eaque eaque quidem. Distinctio rerum recusandae commodi corrupti nostrum. Hic 1325-11-20 repellat a provident. Laboriosam eligendi porro eveniet sint aperiam. Dolores ab aliquam officiis fuga 1555-11-29 reiciendis. Nemo eligendi dignissimos exercitationem. Delectus modi sit officia minus quam.                                                                                                                                                                                                                                         Veniam quos sint. 1647-03-16 voluptates tempora libero doloribus atque accusamus. Ipsam voluptatibus odit similique nesciunt dicta. Architecto praesentium placeat quia. Possimus veniam veritatis illum at voluptate sunt. Explicabo quod nesciunt minima molestias eum ut. Cumque fugiat 1383-02-22 dolorum qui.                                                                                                                                                                                                                  Quos facilis quos quaerat architecto doloribus asperiores facere. Aut tempora nesciunt repellat dolorem. Modi accusamus cupiditate ipsa minima quia alias. Non ratione corrupti qui cum quos rerum. Veritatis dolorem sunt officia dolores nobis voluptatibus. Repellendus aperiam quibusdam ad laboriosam ipsa. Culpa temporibus quaerat eveniet iusto. Asperiores enim reprehenderit natus. Sint repellendus aut possimus quas molestias. Voluptatibus sunt accusantium dolorum. Reprehenderit numquam necessitatibus 1547-10-21 quod. Autem labore delectus. Suscipit blanditiis ut saepe enim aperiam.                                                                                                                                                                                                                                                                                  Praesentium excepturi ducimus reiciendis blanditiis nesciunt expedita. 2020-05-01 quisquam non quam atque 1615-04-05T16:06+12:00. Voluptates deleniti accusamus minus consequuntur magnam ab. Id aliquid cupiditate quaerat inventore. Assumenda inventore asperiores 1615-04-05T16:06+12:00. Sunt quasi itaque suscipit blanditiis. Atque eius quae ad possimus dignissimos expedita.                                                                                                                                                                                                                                                                                                                          Aliquid pariatur excepturi dolorem necessitatibus occaecati. Tempora blanditiis cumque eius autem non voluptates. Alias laboriosam quas possimus ratione blanditiis expedita. Molestiae eius ratione tenetur ipsum possimus doloremque. Sapiente 1109-03-14 ipsam 1544-13-02T02:32+00:00. Facere at cupiditate recusandae. Voluptas voluptates sequi voluptatum. Asperiores impedit iusto vitae dignissimos itaque velit delectus. Quidem rerum dolore amet consectetur. Libero esse vero dolorem inventore minus distinctio facilis.                                                                                                                                                                                                                                                                                                                                                       Laboriosam odit quibusdam officiis 1099-10-21T18:31 odio. Magnam saepe tempora soluta est voluptatibus error. Modi quaerat recusandae. Fugiat tenetur nemo ad. Rerum dignissimos mollitia omnis. Voluptas culpa eveniet doloribus. Similique cum 2037-01-24 doloremque enim. Provident aspernatur praesentium laboriosam reiciendis. Illum optio architecto dicta reiciendis quaerat.                                                                                                                                                                                                                                                                                                                           Culpa ipsa impedit fuga 1596-08-28 numquam temporibus doloremque. Sequi ullam eum impedit perspiciatis. Quas modi doloribus. 1398-03-21T19:51 cupiditate corrupti nulla quis culpa possimus quos. Odit veritatis animi reprehenderit expedita saepe occaecati. Neque quis corrupti quis alias voluptatum nemo. Facere iusto dicta facilis voluptas. Veniam nesciunt tempora. Eos reprehenderit quod quaerat. Est aliquid consequuntur cumque non illo. Totam fugiat ratione iusto. Dolore nisi exercitationem quis harum repudiandae voluptas. In iure ea blanditiis.                                                                                                                                                                                                                                                                                                                       Fugiat fugiat ab. Similique nobis exercitationem enim suscipit ipsam optio. Omnis laboriosam distinctio atque. Sit quia excepturi quae excepturi iusto. Aliquam minus quam nisi numquam natus eligendi asperiores. Sequi tenetur nostrum. Quis alias expedita at praesentium deleniti tenetur. Maiores assumenda nihil ad fuga. Porro ullam officia aut modi 1060-09-11T02:05. Iusto dicta repellat adipisci. Nisi veniam doloremque repellendus rerum quaerat consequatur. Itaque adipisci praesentium numquam quas vitae fugiat. Aliquid totam at.                                                                                                                                                                                                                                                                                                                                        Quae rerum iste eos nemo maxime fugiat. Odit ex sint deleniti beatae ut. Molestias pariatur praesentium magnam. Sit sint dicta fugiat eveniet. Cum amet quam magnam numquam. Eveniet consectetur voluptatibus consequuntur reprehenderit repellat ipsa neque.                                                                                                                                                                                                                                                                       Autem magnam quas sapiente sed suscipit accusamus vel. Explicabo optio consequatur molestias reprehenderit voluptatibus. Corrupti debitis sint eos ipsum odit. Odit et consectetur illum aliquam deleniti molestiae corrupti. Pariatur dolorum ipsum illum enim nisi. Exercitationem architecto quos non impedit illo numquam. Fugiat similique quod. Dicta mollitia omnis ipsum facilis ab. Saepe unde vero veritatis deleniti. Animi dolor distinctio at.                                                                                                                                                                                                                                                     Fuga impedit a eligendi. Assumenda 1027-05-28 quae consectetur. Dolorum possimus 1439-07-05 rem ea. Dolorem expedita repellendus. Corrupti iusto pariatur voluptatum quo corrupti. Ipsam voluptatum quibusdam nisi assumenda quod. Vero ad dolor reprehenderit. Repellendus necessitatibus sit aperiam. Deleniti tenetur recusandae ad. Quia sapiente 1027-05-28 id fugiat commodi.                                                                                                                                                                                                                                                                                                                             Temporibus excepturi quod quos ex autem. Quisquam laborum fugit tempore eligendi incidunt pariatur cumque. Soluta perspiciatis veritatis nisi. Officiis aperiam deleniti placeat repellendus ullam quae. Labore nemo aut eaque vel. Ipsam non at exercitationem maiores magni modi. Magnam distinctio repellat architecto. Doloremque consequuntur dignissimos dolore hic voluptatum 1807-01-11. Possimus delectus repellat pariatur voluptates. Officiis placeat harum sint assumenda praesentium. Aspernatur maiores eaque repudiandae asperiores. 1385-08-21T09:11 voluptatum asperiores totam ipsa. Maiores sapiente voluptates reprehenderit harum fugit.                                                                                                                                                                                                                              Voluptatem debitis deleniti id rem. Blanditiis voluptatum velit. Veniam quisquam nostrum vel 1589-10-02 laudantium hic. Et voluptatum necessitatibus voluptate similique. Totam error minima voluptas. Magni voluptate repellat.                                                                                                                                                                                                                                                                                                    Aspernatur eos libero libero illo placeat. Error velit architecto architecto. 1461-11-08 commodi praesentium saepe tenetur expedita odit. Voluptate ipsa a iure neque eveniet quisquam. Non necessitatibus ad temporibus magni. Placeat iure eligendi adipisci necessitatibus blanditiis voluptatibus. Incidunt hic aspernatur natus provident culpa. Amet cumque asperiores qui. Fuga nulla inventore non magni. Cum possimus ab optio id. 
"""

date = []
diff = []
regex = re.compile(r"(?P<Year>\d\d\d\d)-(?P<Month>\d\d)-(?P<Day>\d\d)(?P<Hour>T\d\d:\d\d:\d\d)?(?P<TZ>\d:\d)?")
birthday = datetime.date(2000, 4, 18)

for datereg in regex.finditer(text):
    try:
        date.append(datetime.date(int(datereg.groupdict()['Year']), int(datereg.groupdict()['Month']), int(datereg.groupdict()['Day'])))
    except ValueError:
        continue

for difference in date:
    diff.append(abs(birthday - difference))

print("Data mais próxima é:", date[diff.index(min(diff))], "\nA diferença em dias é de:", min(diff).days)