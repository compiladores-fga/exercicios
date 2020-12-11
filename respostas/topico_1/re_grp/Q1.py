import re
import datetime

text = """
Odit soluta temporibus quam exercitationem quasi ullam. Dicta consequatur laudantium minus voluptatum eaque soluta. 
Provident odio nobis. In dolor 1558-06-01 dicta 1157-02-29. Exercitationem deleniti nam at vitae. 
Mollitia harum explicabo consequatur voluptate nulla. Voluptas non porro corrupti unde. Voluptate minus velit iure repudiandae. 
Numquam laborum nemo eligendi est numquam.

Autem explicabo rerum quidem rem explicabo quaerat 1747-05-28T03:07:30. Laborum nihil ad neque incidunt dolores. Sunt vero id. 
Aspernatur corrupti adipisci nesciunt temporibus sapiente sint. Veniam tempore dolores neque 1736-09-15. 
Dolores maxime neque quibusdam perferendis nostrum cumque reprehenderit. Suscipit cum eligendi ipsa. Repudiandae in ex nemo. 
Consequatur dolor occaecati iusto sapiente. Hic dignissimos assumenda accusamus voluptatibus autem. Laborum pariatur natus sunt. 
Eaque 1747-05-28T03:07:30 adipisci. Eum doloremque 1747-05-28T03:07:30 velit modi sit voluptatibus.

Voluptatum libero cum earum magnam aliquam quo. Iusto excepturi modi id. Aspernatur dolore laudantium. 
Itaque aspernatur quasi laboriosam 1113-10-18 culpa. Occaecati commodi iste. Explicabo laudantium asperiores sapiente iste et. 
Sapiente hic ut ratione.

Nisi iure dolores aspernatur velit eveniet debitis dignissimos. Tempore reiciendis sequi odit nemo occaecati voluptate. 
Necessitatibus atque earum a. Dolorum praesentium totam. Aspernatur occaecati rerum debitis numquam officia incidunt ipsa. 
Amet dolorum tempora facere. Labore placeat eius harum provident consectetur sit quas. In debitis dolores doloremque eum voluptates culpa. Repudiandae nesciunt dolores officia vitae ullam. Totam sapiente sint quibusdam. Dolorem consectetur unde tempora iure sint at provident.

Voluptatibus asperiores ipsa. Animi numquam in asperiores doloremque repellat tempora. Est tempora ab adipisci earum ullam. 
Voluptatem rerum repudiandae neque. Minima dicta quod nisi vitae. Tempore eum velit occaecati dicta pariatur. Ex aut consequuntur. 
Provident ipsum corporis soluta quas cupiditate provident. Sunt error sint corporis mollitia voluptates recusandae. 
Ut rerum omnis quisquam repellendus repellat quos eveniet.

Dolorum atque dolore. Dolore qui nostrum est quam autem unde. Accusamus recusandae nihil animi ipsa excepturi reiciendis ab. 
Accusamus 1555-10-18 facilis tempore nulla ipsa reprehenderit quae. Quam dolorum accusamus incidunt natus perferendis. 
Quod eaque nesciunt. Maxime deserunt maiores in aperiam nihil 1744-09-14T06:52:11. Totam provident blanditiis nobis nobis. 
Laborum 1782-03-22 porro a deleniti. Eius 1555-10-18 aperiam sapiente molestias facere. Maiores ab exercitationem eos.

Mollitia in fuga adipisci nulla vero ullam. Aperiam ullam ratione aut iusto beatae reprehenderit. 
Numquam 1874-01-05T12:49:42+16:00rat tempore aut odio corporis. Iusto nemo tenetur excepturi ullam. 
Ullam 1874-01-05T12:49:42+16:00 neque rerum possimus magnam. Deleniti atque fugiat suscipit labore soluta necessitatibus nihil. 
Nobis dolorem laboriosam dicta libero assumenda eos. Exercitationem a quas ipsam 1656-06-11 odio a. Commodi vitae unde consectetur. 
Minus vitae exercitationem. Illo porro eligendi dolorum. Ut excepturi explicabo perspiciatis unde amet quasi. 
Animi sed laboriosam earum explicabo minima quia quisquam.

Voluptatum laborum provident recusandae veritatis 1753-08-02T05:04:23+24:00 veniam sit. Soluta qui temporibus aut. 
At nobis quidem vitae repellendus adipisci. Corporis in ab aspernatur tempore fugiat. Laborum ullam amet quia. 
A voluptates perferendis 1821-05-20T01:13:03+01:00 quasi animi. Mollitia non nostrum facere.

Eaque alias exercitationem dist1812-04-24T13:22:46ctio. Laboriosam numquam iusto nesciunt quod sunt. Exercitationem nam dolorem. 
Debitis amet veritatis labore. Aliquam 1812-04-24T13:22:46 autem suscipit 1812-04-24T13:22:46ventore veritatis 1812-04-24T13:22:46. 
Officiis 1812-04-24T13:22:46cidunt provident. Quas enim nostrum laudantium rem eaque. 
Magnam veritatis dolorem quos aliquid 1577-02-02. Laborum quibusdam doloribus placeat. 
Molestiae porro iure a reprehenderit blanditiis quas. Neque optio molestiae nam. Explicabo odio recusandae voluptate iusto dolor. 
Inventore unde similique pariatur.

Ipsa qui 1203-10-14 laudantium ex. Pariatur numquam praesentium accusantium quaerat architecto in dignissimos. 
Cum aliquam fugiat libero recusandae ab temporibus. Reprehenderit vero quia perferendis deserunt. At modi est. 
Iure hic nulla voluptate cumque. Autem assumenda rerum voluptatibus cum tenetur commodi. Aut quos laudantium enim doloremque. 
Animi assumenda sequi. Voluptatem in praesentium autem porro pariatur occaecati odit. Quaerat veniam fugit 1058-05-31.

Debitis dignissimos temporibus sit alias temporibus at. Omnis esse consequuntur. Sapiente consequatur qui fugiat. 
Veritatis laboriosam esse dolorem modi minima. Similique deleniti ab vitae sequi eaque velit. 
Dignissimos ipsam exercitationem repudiandae aliquam similique. Atque dolor perferendis amet laboriosam natus aperiam dicta. 
Nihil deleniti dolore tempore distinctio quia.

Impedit dolorem occaecati suscipit. Molestias incidunt accusantium. Officiis facere magni atque. Doloremque provident 1650-04-23. 
Optio corporis sol1025-08-28a excepturi maiores expedita. Dicta officia aspernatur mollitia amet voluptate odit. 
Voluptas laudantium aperiam consequuntur. Tenetur fuga reprehenderit 1143-05-20 minus 1025-08-28 sed nostrum. 
Fuga voluptate eius animi 1143-05-20 sit. Odit recusandae illum 1025-08-28 libero a saepe recusandae. 
Fuga tempora nostrum quos numquam aliquid sit vitae.

Labore dolorum excepturi. Veniam nobis asperiores voluptates deleniti sapiente. Ipsam 1905-01-04 asperiores aut laborum tenetur. 
Similique ex occaecati laudantium voluptas hic excepturi ullam. Corrupti vel asperiores eligendi odio laudantium. 
Nostrum mollitia sunt recusandae porro ab quos. Aperiam voluptatibus quae fuga impedit aperiam. 
Necessitatibus quaerat quos 1905-01-04 commodi voluptatibus expedita. Necessitatibus nesciunt beatae. 
Expedita minus hic porro ex.
"""


regex = re.compile(r"(?P<Y>\d\d\d\d)-(?P<M>\d\d)-(?P<D>\d\d)(?P<H>T\d\d:\d\d:\d\d)?(?P<TZ>\d:\d)?")
date = []
dif = []
birthday = datetime.date(2000, 6, 21)
#
#dates = []
#for i in list(date.finditer(text)):
#    date.append(datetime.date(i))

#print(list(regex.finditer(text)))
#print(len(list(regex.finditer(text))))

for m in regex.finditer(text):
    try:
        date.append(datetime.date(int(m.groupdict()['Y']), int(m.groupdict()['M']), int(m.groupdict()['D'])))
    except ValueError:
        continue

for m in date:
    dif.append(abs(birthday - m))

print("Data mais próxima é", date[dif.index(min(dif))], "com", min(dif).days, "dias de diferença!")



