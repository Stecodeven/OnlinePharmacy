## Software Engineering Project
***

#git综述：
分布式版本控制系统 这样的名字并不能让人一听就知道做什么。

希望系统一点学习git知识和命令可以访问（廖雪峰老师的git教程）：
https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000

简单易懂，易上手，其实就是把命令含义了解一遍，敲一遍。
原理搞清楚。学习成本比较低。
随便拿一块的时间比如2小时，就能过一遍。

如果觉得总是记不住命令，不用着急，因为这些就是用得多了，就成习惯了。


# 针对项目成员的git 使用：

# 1基本环境部署
	

	比如你现在正在main目录下
	克隆本项目  
		git clone git@gitee.com:Callmejp/OnlinePharmacy.git

	此时远程仓库的项目所有文件都已经克隆到本地了。
	项目成员可以根据情况作出任意修改

# 2分支的意义
	

	远程的仓库首先有两个分支，一个叫master核心分支，一个叫dev，项目一开始创建的时候
	只有一个master，dev是我们在网页手动创建的。不变了，就只需要这两个分支。

	master就是用来放我们软件的稳定版本的，我们一般修改，操作，都是在dev上进行，
	只有dev上进行的差不多了，我们才把dev内容同步到master上，或者说叫合并。

	可以把dev当做master背后的艰辛努力，为了玩耍，
	我们复制了master内容，dev上各种修改，修改好了，再同步到master，
	master就是我们只愿意给用户看的成功版本。
	master就是我们的成品，dev就叫成功的背后的刻苦吧，好尬。。。

	
	克隆下项目以后目录结构应该是main/OnlinePharmacy
		cd 到OnlinePharmacy下

	其实会有一个.git文件夹
	(接下来你的命令就都是在这个项目文件夹下进行了)
	
	这个事实上是你的本地git仓库，你所做的修改，提交，
	只要还没push，你本地最终的版本都是在你本地的仓库里
	只有你push了以后才会上传到远程仓库

		git branch 回车

	你会只看到一个master分支
	因为之前默认只把远程的master给克隆下来了。
	这个时候需要
		
		git checkout -b dev origin/dev 回车
	
	这样创建了本地的dev分支(-b就是创建)
	并且还和远程的dev分支关联了！关联的意义后面再讲
	（origin就是本项目关联的远程仓库的名字
	看到origin就能想到远程仓库，可以用
		git remote -v
	来查看关联的远程仓库。

	然后
		git branch 回车

	你会看到两个分支，并且也知道自己在什么分支
	(没事都可以敲敲git branch查看自己在什么分支 有哪些分支)
	git branch是比较重要的命令！


# 3多人协作
	

	划重点！！!
	记住你现在在dev分支。git branch可以查看你在哪个分支
	如果不在dev请用git checkout 分支名  切换到dev。
	
	然后
		git pull 
	表示把远程仓库的dev最新内容抓取到本地的dev
	然后你再开始工作。

	比如你本地写好了一个html或者py文件
	先到文件所在目录 类似于svn实验的操作

		git add test.html 
		git add views.py
		git commit -m "This is a commit test"

	git add 就是把你自己更改过的，想更新的放到本地一个暂存区中
	可以多次add，然后commit只用做一次，提交到你本地的git仓库中。
	前面#2里说过只要还没push，提交的都是送往本地git仓库。
	commit后面的-m一般都得加，省了要报错，message的意思，就是你提交
	的时候的留言，这次提交简单说干了什么。这些都是可以调出来看的。

	最后
		git push origin dev

	这样把本地的dev分支内容和远程的dev内容同步了。

============================================

	以上是比较简单的场景。稍微复杂一点情况是必须掌握的。

	事实上，可能会出现这样的情况：
	JP在他的本地dev分支上修改了 a.py文件
	并且提交commit然后push到了远程
	
	之后我也在本地的dev分支修改了 a.py文件
	但是晚于JP的push，当我正准备push的时候，commit好了以后

	我在本地输入 git push origin dev后报错了
	这是因为我和JP的push时间差导致当我push的时候远程库和我的库不一致
	这时候操作很简单。
		git pull
	把远程dev最新的同步下来，因为JP已经把他的最新放在远程dev上了
	然后git的机制就是在起冲突的那个文件里会把我改的部分和最新的JP
	改过或者添加的部分都给注明出来。

	文件当中它自动的用显眼的标签注明出来。

	然后我打开a.py,手动的合并我和JP各自修改过的那部分内容。
	然后我再次在本地
		git add a.py
		git commit -m "test"
		git push origin dev
	这次就会push成功，就是我和JP都改过且手动合并的版本。
	线上的仓库就是我和JP都改过的版本了（事实上是我最后合并了两个文件并push的

	简言之，同一文件 后push的那个人工作会稍微多一点。


	以后要在dev分支下工作的时候，最好先
		git pull
	保持和项目最新dev分支的一致


# b话
	

	本操作说明有许多需要改进的地方，因为我自己(zzp)就是半罐水，临时写的。
	希望小伙伴觉得有可以改动的，表达不到位的，或者有错误的，都直接改改，因为
	这文件本身也可以多人协作更改的嘛，然后改完提醒我一下，让我也完善下自我，感激不尽。

	还有很多不熟悉，局限，不到位的地方。因为git命令很多，我把能想到，暂时可以先用着的
	写了下来，如果这个操作流程之类的没太看明白，很可能是因为很多原理性的地方没解释清，逻辑关系没给大家理顺，要么一笔带过，要么就没提，限于篇幅，这样的情况下还是建议大家去看看系统一点的教程。











这个文档既然是Stecodeven先写的，那么有必要调皮地留下浅薄的孤陋寡闻的我通过一位长者才了解到的深得蛤心的诗：

												苟利国家生死以，
												岂因祸福避趋之。
//其他都能删这诗不准删:)


