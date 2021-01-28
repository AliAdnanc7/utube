
class Messages:

    START_MSG = "Hi there {}.\n\n     مرحبا بكم في بوت رفع الى يوتيوب\n  للتواصل @AliS219  \n لمعرفة التعليمات اكتب \n\n /help"

    HELP_MSG = [
        ".",
        "Hi there.\n\nFirst things first. You should be aware that youtube processes each and every video uploaded, and its AI is amazing that it flags the video for copyrights if it finds copywrited content as soon as its uploaded, and you will not be able to publish the video.\n\nRead through all the pages to know how I work.",

        "**Lets learn how I work.**\n\n**Step 1:** __You authorise me to upload to your youtube channel.More about this in comming pages.__\n\n**Step 2:** __You forward any Telegram video to me.__\n\n**Step 3:** __You reply __/upload __to the forwarded video file.You can also specify some title in the upload command, but its optional though.Title will follow the __`/upload`.__If no title is given, filename will be used as title.__\n\n**Step 4:** __I remotely download the file and uploads to your Youtube channel.__\n\n**Step 5:** __I send you the Youtube link after upload.__",

        "**Create your youtube channel**\n\nThere is no point in using me if you dont have a Youtube Channel.So go through the given steps to create one.\n\n**Step 1:** __Sign in to YouTube on a computer or using the mobile.__\n\n**Step 2:** __Try any action that requires a channel, such as uploading a video, posting a comment, or creating a playlist.__\n\n**Step 3:** __If you don't yet have a channel, you'll see a prompt to create a channel.__\n\n**Step 4:** __Check the details and confirm to create your new channel.__",

        "**Verify your YouTube account**\n\nYoutube take spam and abuse very seriously. So you are asked to verify your Youtube account. Once you've verified your account, you will be able to upload videos longer than 15 minutes. If you haven't verified your account every video uploaded which are longer than 15 minutes will be removed.\n[Verify your Youtube account here.](http://www.youtube.com/verify)\n\n__Remember to verify your project, else your uploads will be kept private.__",

        "**Now lets authorise.**\n\nYou need to give me the access to upload videos to your Youtube account.For that open the given link and allow access and copy the code. Come back here and type `/authorise copied-code` and send it.\n\n**Fear not!**\nI'm not a hacker or someone who wants to creep into people's privacy. I respect one's privacy. I'm here just to help anyone who wants help. If I was a hacker I won't be sitting here writing Telegram Bots."
    ]

    NOT_A_REPLY_MSG = "يجب رد على فيديو ليتم عملية الرفع"

    NOT_A_MEDIA_MSG = "لم اجد الفيديو \n\n "+NOT_A_REPLY_MSG

    NOT_A_VALID_MEDIA_MSG = "هذه ليست وسائط صالحة"
    
    DAILY_QOUTA_REACHED = "انا يمكن ان ارفع 6 فيديوهات باليوم  فقط .. عملية فشلة ... اصبر لليوم ثاني "

    PROCESSING = "...يتم المعالجه "

    NOT_AUTHENTICATED_MSG = "لا تمتلك توكن قناة حاليا ... اكتب /help   /n/n ليتم عملية الاضافه"

    NO_AUTH_CODE_MSG = "هذا ليس توكن القناة ..... تحقق من توكن القناة"

    AUTH_SUCCESS_MSG = "تمت عملية ربط توكن بنجاح ... استعد للرفع فيديوهات"

    AUTH_FAILED_MSG = "فشل في عملية الربط\nDetails:{}"
    
    AUTH_DATA_SAVE_SUCCESS = "تم حفظ توكن القناة بنجاح"
    
