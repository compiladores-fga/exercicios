import re

if __name__ == "__main__":
    text = """
            <!DOCTYPE html>
            <head><title>Lorem ipsum</title></head>
            
            <body>
            <p>Atque sit natus. <img src="/officiis/error.gif"> fugit dignissimos sequi quis. Fuga animi voluptas doloribus officiis quod quibusdam. Ipsum veritatis quos dolore molestiae illum nesciunt. Unde ex voluptatem voluptates minus vel provident. <img src="/officiis/error.gif"> dolore eos eos doloremque libero nisi. Odio quas eos eos minus.
            
            <img src="/harum/placeat.gif">
            
            <img src="/cumque/suscipit.gif">
            
            <h3>Quibusdam id vitae corrupti hic</h3>
            
            <img src="/voluptate/repudiandae.gif">
            
            <p>Quidem quae facere delectus illo in. Sapiente sit corrupti labore in iusto enim. /sit/suscipit.gif porro vitae soluta rerum. Aliquid dolore deserunt vel numquam incidunt. Unde ad amet quidem consequatur facere quisquam. Eveniet dolores molestiae illum quibusdam repudiandae nesciunt nisi. Modi iusto aliquam magnam. Sit esse ea facere. Iusto commodi autem eligendi aliquid harum.
            
            <img src="/repellat/reprehenderit.bmp">
            
            <p>Illo sunt deserunt eos doloribus odio. Nulla cum illo ipsam totam error fugit rem. Alias <img src="/beatae/impedit.gif"> illum molestiae quibusdam ea id. Earum voluptatem consequuntur accusantium. Tenetur autem deleniti laboriosam illo perferendis. Minus dolores impedit a. Magnam blanditiis eaque cum. Saepe quia alias explicabo non quae ut. Nemo commodi vel iste velit est ullam amet. Ad molestiae vel perferendis aperiam. Ratione maxime amet iste ipsa quo incidunt. Ad quos nostrum distinctio. Ad provident at.
            
            <img src="/illo/tempore.gif">
            
            <p>Ducimus officia laborum laborum doloremque. Earum facilis eveniet ex. Facilis iste fugiat cupiditate assumenda magnam repellat quo. Atque accusamus est ad. Delectus ipsa hic incidunt. Odit dolor tenetur nostrum consequatur dolorem dolore. Porro consequatur debitis quae sit. Pariatur doloremque nam ratione. Possimus incidunt hic deleniti. Esse magni commodi dolorem /natus/alias.jpeg. Minus dolorem commodi sit asperiores nemo. Quo soluta quo. Saepe veritatis dolorum facilis consectetur vero necessitatibus.
            
            <p>Voluptas officia adipisci repudiandae. Eaque sunt deserunt. Ad omnis voluptatem maxime alias. Illum sit libero quod. Sint quisquam quos necessitatibus omnis aut dolorum. Expedita iste commodi iure laboriosam. Explicabo consequatur corrupti explicabo. Quisquam explicabo recusandae doloribus. Nemo aliquid consectetur nihil excepturi. Dolor aspernatur mollitia vitae nemo saepe. Veniam iure incidunt fugiat accusantium. Placeat dicta nobis architecto magni.
            
            <p>Ipsa quaerat minus dolorum. Eum doloremque eum natus aspernatur sit impedit. Consequatur fugit nulla nisi dolore. Eveniet deserunt fugiat id provident non adipisci unde. Incidunt optio architecto dolorum. Suscipit harum et labore.
            
            <p>Repudiandae necessitatibus expedita soluta. Expedita ipsa assumenda. Veniam rerum <img src="/saepe/harum.tiff"> hic. Rerum ipsam eos <img src="/saepe/harum.tiff"> beatae deleniti. Culpa autem quasi officia aliquam. Consequatur earum deserunt placeat esse numquam. Fugiat excepturi perferendis velit error. Explicabo adipisci sequi earum officiis.
            
            <img src="/non/ullam.gif">
            
            <img src="/fugit/fugit.gif">
            
            <p>Ea placeat ut ea distinctio nihil voluptate sint. Eum iusto quidem sequi iure pariatur. Aliquid minima quas ex vel. Asperiores asperiores ex repudiandae molestias. Earum atque architecto incidunt. Nam minima explicabo possimus. Sit quos at sit delectus repellendus. Adipisci aliquid ut minima illum. Assumenda occaecati est ipsum blanditiis. Tempore libero porro laborum fugit consectetur.
            
            <p>Alias dolorem laudantium illum. Vel suscipit praesentium. Dignissimos deleniti veniam placeat. Saepe reprehenderit doloribus illum ab corrupti libero. Commodi dolorum assumenda esse fugit modi voluptates. Nam ad saepe voluptatem perferendis natus. Expedita quaerat itaque sit eligendi <img src="/nostrum/cumque.gif"> quibusdam. Ipsum impedit suscipit vitae excepturi vel.
            
            <p>Culpa porro animi ea. Ducimus inventore exercitationem. Voluptas iure vero dignissimos nobis aliquam nulla. Doloremque consequuntur pariatur recusandae. Nobis eaque libero tempore aspernatur. Illum suscipit <img src="/perspiciatis/cum.tiff"> iste saepe voluptatibus iste sequi. Aperiam nemo cupiditate accusamus dicta iure. Ex repudiandae blanditiis laudantium quis qui laborum velit. Temporibus nisi perspiciatis nemo ullam. Rem libero maiores. Numquam recusandae nostrum. Dolorem voluptate consectetur eum in est aliquam. Sapiente nulla illum.
            
            </body>
            """
    gif_regex = r'<img\ssrc="([\d\w\/]+\.gif)">'
    gifs = re.findall(gif_regex, text)
    print(len(gifs))
