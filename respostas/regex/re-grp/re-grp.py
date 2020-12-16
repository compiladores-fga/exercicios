import datetime, re

if __name__ == "__main__":
    text = """
            Perferendis deleniti nemo ipsam consectetur eligendi. Labore quis iusto atque inventore. Architecto nihil deserunt quia eos. Consectetur dolorem nulla ab eius qui. Consectetur ab modi recusandae laboriosam dolorum. 1069-05-12T23:04+17:30 aut eum doloremque 1682-02-12 1477-11-15T24:46 iure. Mollitia illum animi asperiores ducimus quas odit cupiditate.

            Quis necessitatibus possimus adipisci quam voluptatibus nobis aperiam. Amet sint perferendis sed pariatur. Pariatur laudantium aliquam at velit. Mollitia repellendus molestiae illum nam. Sequi consequuntur ex explicabo. Error adipisci hic quidem. 1292-06-23T17:16+23:30 labore perspiciatis velit. Cupiditate aperiam necessitatibus consequuntur delectus enim. Nihil ex neque veritatis perferendis saepe aliquam. Accusamus distinctio doloremque eum maiores animi blanditiis. Amet animi in eum occaecati. Dolorem eos rerum similique quod at.
            
            Perferendis 1083-04-06 ipsam cumque. Quis fugit voluptate error qui. Magnam commodi libero doloremque assumenda minima sed. Eum asperiores quam 1083-04-06 ea. Doloribus ullam eveniet quae iure. Officia officia odit praesentium sequi deserunt.
            
            Commodi numquam qui voluptatibus totam deleniti placeat. Saepe numquam officiis aliquid eius unde sequi. Accusantium eos fugiat rerum eaque sequi. Iste quasi laudantium ratione distinctio quia. Officia laboriosam dolorem pariatur expedita sit. Id necessitatibus nemo exercitationem velit tempore. Corrupti tenetur 1674-09-22T08:26 rem ea. Sed necessitatibus expedita veritatis magnam minus debitis. Dolorum adipisci itaque officiis facere hic. Maxime facere incidunt voluptate accusamus. Deleniti minus suscipit veniam modi possimus. Aut voluptatem excepturi accusantium. Facere accusamus pariatur tenetur soluta officiis eius.
            
            Eius velit exercitationem hic magnam dolores. Numquam dignissimos similique. Qui deserunt odio ab repellat. Dolor illo officiis quaerat quisquam. Quisquam nostrum necessitatibus voluptate repudiandae. Consequuntur ut beatae doloribus porro illum repudiandae. Ad officiis quam sequi totam maxime. Mollitia provident rem necessitatibus quos perferendis 1900-02-17T13:26.
            
            Nemo quae ipsam deserunt illo temporibus. Quis id possimus id. Quisquam debitis esse id fuga reiciendis nihil 1381-04-15T03:59+03:30. Quibusdam 1765-12-09T13:20 quas dolorem. Adipisci numquam pariatur. Est ad tempora.
            
            Consequatur eius vitae autem ducimus. Quis saepe nam fuga. Quam iste repellendus voluptatem doloribus aut commodi voluptatibus. Sint beatae dolores eveniet exercitationem voluptates. Labore impedit eius consectetur. Commodi magni unde labore illo quae cum. Impedit vero illo. Quia earum possimus nesciunt tempore et reprehenderit. Nisi nostrum laudantium cum.
            
            1200-08-14 sint veniam expedita quos provident consequuntur. Dignissimos illo illo ullam nostrum. Architecto nisi praesentium impedit quo quam in. Laboriosam inventore est vitae culpa inventore laboriosam illo. Ipsam repudiandae accusantium eius. Culpa nesciunt cumque aliquid. Doloremque perspiciatis maxime aspernatur. Voluptate ut cum quod placeat. Eligendi quas nemo veniam nobis nostrum. Impedit veritatis illo sequi laboriosam dolorem laborum. Nisi iste voluptatibus non. Voluptatibus laudantium fuga est neque voluptate optio voluptates. Distinctio aspernatur dolor quo officiis reprehenderit.
            
            Dicta alias ut maxime. Id sint voluptate pariatur esse. Magnam facere corrupti voluptatem adipisci excepturi. Quas 1812-12-19T19:34 aliquid quis temporibus tenetur. Necessitatibus 1070-07-18 odio et soluta perferendis laborum optio. Nemo adipisci autem. Repellendus provident similique deleniti. Exercitationem minima non nulla corrupti eum magnam. Enim sapiente eos voluptatum nulla aspernatur. Consequuntur nihil recusandae perspiciatis aliquam in. Animi vero at deserunt voluptatum explicabo. Modi ratione aspernatur corrupti inventore optio modi.
            
            Quisquam 1987-03-13 quis magnam voluptates ipsam. Minus dolore 1096-06-01T13:06 reiciendis minima accusamus pariatur. At possimus beatae nesciunt 1442-10-10 occaecati. Itaque eius doloribus vel. Eos perspiciatis labore. Dolores voluptates cumque aspernatur quam ex tempore.
            
            Nam nobis assumenda velit. Vel illo quaerat voluptatem inventore nisi aliquam earum. Doloremque 1463-03-04 modi autem maiores error aliquam. Error expedita 1928-02-13T13:42 delectus quod reprehenderit. Itaque quaerat beatae quaerat velit fuga. Animi saepe consequatur aliquam accusantium delectus dolores. Architecto distinctio nisi eaque iusto porro dolor. Perspiciatis esse eveniet. Perspiciatis reiciendis veritatis. Beatae perspiciatis totam ratione sequi consectetur. Tempora autem praesentium similique. Ut ipsam repellat autem 1463-03-04.

            """

    birthday = datetime.date(1997, 11, 8)

    regex = re.compile(r"(?P<year>\d\d\d\d)-(?P<month>\d\d)-(?P<day>\d\d)(?P<H>T\d\d:\d\d:\d\d)?(?P<TZ>\d:\d)?")

    dates = []
    print(dates)

    for date in regex.finditer(text):
        try:
            dates.append(datetime.date(int(date.groupdict()['year']), int(date.groupdict()['month']), int(date.groupdict()['day'])))
        except ValueError:
            continue

    dates_dist = []
    for date in dates:
        dates_dist.append(abs(birthday - date))

    closest_date = dates[dates_dist.index(min(dates_dist))]

    print("A data mais próxima de", birthday, "é", closest_date)
