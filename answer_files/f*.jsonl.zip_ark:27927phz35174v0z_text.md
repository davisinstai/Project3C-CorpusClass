# ark://27927/phz35174v0z

MATEC Web of Conferences 201, 04004 (2018) https://doi.org/10.1051/matecconf/201820104004
ICI 2017
© The Authors, </i>published<i> by EDP Sciences. This is an open <b>access</b> <b>article</b> </i>distributed<i> under the <b>terms</b> of the Creative Commons Attribution 
License 4.0 (http://creativecommons.org/licenses/by/4.0/).
* Corresponding <b>author</b>:  meilingj@mail.tku.edu.tw 
Smart Learning of Porn Fake News in the Family-Friendly Filters 
Meiling Jow1,*, and Yaojung Shiao2 
<b>1Department</b> of Information and Communication, Tamkang University, Taipei, Taiwan 
2National Taipei University of Technology, Taipei, Taiwan 
Abstract. The <b>proliferation</b> of fake <b>news</b> on Facebook and Google has been a hot-<b>button</b> <b>topic</b> after the 
2016 US presidential <b>election</b>. Fake <b>news</b> <b>phenomenon</b> is not </i>limited<i> in the political <b>sphere</b>. The <b>porn</b> 
<b>industries</b> have been </i>using<i> <b>affiliate</b> <b>marketers</b> to </i>send<i> fake <b>news</b> to </i>reach<i> more <b>consumers</b>, even <b>children</b>. 
Easy <b>availability</b> of <b>pornography</b> for <b>children</b> on the <b>internet</b> has been an <b>issue</b>. In US, the average <b>age</b> of 
<b>exposure</b> to <b>porn</b> is 11 to 12. Frequent <b>exposure</b> to <b>pornography</b> may </i>lead<i> to <b>normalization</b> of harmful 
<b>behaviors</b>. </i>Starting<i> late 2013, <b>internet</b> <b>service</b> <b>providers</b> in Britain </i>made<i> “<b>family</b>-friendly <b>filters</b>,” which 
<b>block</b> X-</i>rated<i> <b>websites</b>, the <b>default</b> for <b>customers</b>, because <b>kids</b> are </i>exposed<i> to <b>pornography</b> at a young <b>age</b>. 
Google </i>banned<i> pornographic <b>ads</b> from its <b>search</b> <b>engine</b> from July 2014. <b>Prostitution</b> and <b>escort</b> <b>services</b> 
</i>extend<i> its <b>market</b> despite these <b>efforts</b> for the <b>sake</b> of the <b>upsurge</b> <b>porn</b> fake <b>news</b>. <b>Porn</b> fake <b>news</b> is 
</i>produced<i> purposefully to </i>click<i>, <b>share</b>, </i>react<i>, and <b>comment</b>. To </i>mitigate<i> the <b>damage</b> </i>caused<i> by <b>porn</b> fake 
<b>news</b>, </i>designing<i> a fully </i>automated<i> fake <b>news</b> <b>detector</b> is currently infeasible, because the <b>problem</b> at <b>hand</b> is 
too complex for <b>technology</b> alone. Even the <b>subproblem</b> of </i>defining<i> the <b>criteria</b> under which to </i>classify<i> 
<b>news</b> as “fake” </i>creates<i> <b>ambiguity</b> that </i>requires<i> human <b>judgment</b>. The <b>ability</b> to </i>determine<i> whether an <b>article</b> 
is real or fake </i>requires<i> more than just <b>information</b> about the <b>article</b>; it </i>requires<i> an <b>understanding</b> of cultural 
<b>factors</b>, for <b>example</b> “<b>tea</b>” maybe </i>used<i> by <b>prostitution</b> and <b>escort</b> <b>services</b> in Taiwan. This <b>paper</b> </i>suggests<i> 
one <b>way</b> to </i>use<i> artificial <b>intelligence</b> and human <b>judgment</b> to </i>make<i> it more valid to </i>quarantine<i> <b>porn</b> fake 
<b>news</b>. 
1 <b>Introduction</b> 
Fake <b>news</b> currently </i>plagues<i> the <b>world</b>. The <b>proliferation</b> 
of fake <b>news</b> on Facebook, Twitter and Google has been 
a hot-<b>button</b> <b>topic</b> after the 2016 US presidential <b>election</b>. 
Fake <b>news</b> is </i>fueled<i> in <b>part</b> by <b>advances</b> in <b>technology</b>. 
Wonder Woman <b>star</b> Gal Gadot’s <b>face</b> was </i>pasted<i> onto a 
<b>porn</b> <b>actress</b>’s <b>body</b> [1]. </i>According<i> to the Reuters <b>report</b>: 
“from <b>bots</b> that automatically </i>fabricate<i> <b>headlines</b> and 
entire <b>stories</b> to <b>computer</b> <b>software</b> that </i>synthesizes<i> 
Donald Trump’s <b>voice</b> and </i>makes<i> him </i>read<i> <b>tweets</b> to a 
new <b>video</b> <b>editing</b> <b>app</b> that </i>makes<i> it possible to </i>create<i> 
authentic-</i>looking<i> <b>videos</b> in which one <b>person</b>’s <b>face</b> is 
</i>stitched<i> onto another <b>person</b>’s <b>body</b>.” The <b>war</b> to </i>fight<i> 
fake <b>news</b> is not </i>going<i> to be easy. 
Fake <b>news</b> <b>phenomenon</b> is not </i>limited<i> in the political 
<b>sphere</b>. The <b>porn</b> <b>industry</b> has long been </i>using<i> <b>affiliate</b> 
<b>marketers</b> to </i>send<i> <b>porn</b> fake <b>news</b> to </i>reach<i> more 
<b>consumers</b>, among them even young <b>children</b>. Average 
<b>age</b> of first <b>internet</b> <b>exposure</b> to <b>pornography</b> is 11 <b>years</b> 
old, </i>according<i> to <b>research</b>. <b>Dissemination</b> of obscene 
<b>material</b> to <b>children</b> regardless of its <b>form</b> from 
traditional <b>broadcasting</b> is </i>outlawed<i> by almost every 
<b>nation</b> in the <b>world</b>. Criminal Offences </i>relating<i> to the 
<b>publication</b> of obscene <b>material</b> have long </i>existed<i> in 
England. But the <b>distribution</b> and <b>marketing</b> of <b>porn</b> 
<b>industry</b> </i>evolves<i> wisely along with the <b>advance</b> of 
<b>communication</b> <b>technologies</b> to </i>avoid<i> <b>regulation</b>, while 
<b>age</b>-<b>verification</b> <b>requirements</b> for online <b>porn</b> is not 
effectively </i>working<i>. 
<b>Kids</b> are </i>exposed<i> to <b>pornography</b> at a young <b>age</b> on 
the <b>internet</b> because of its easy <b>accessibility</b>. There </i>are<i> 
4.2 million pornographic <b>websites</b>, 12<b>%</b> of all <b>websites</b>. 
Some <b>porn</b> <b>sites</b> </i>get<i> more <b>traffic</b> than <b>news</b> <b>sites</b> like 
CNN. </i>According<i> to the <b>website</b> Paint Bottle, 30 <b>percent</b> 
of all <b>data</b> </i>transferred<i> online is </i>porn<i>. <b>Pornhub</b> is the 63rd 
most visited <b>site</b> on the <b>Internet</b> </i>according<i> to Alexa [2]. 
All <b>kinds</b> of <b>people</b> can </i>access<i> it, whether they are 
<b>minors</b>, <b>adults</b>, or <b>people</b> with psychological <b>problems</b>. 
<b>Children</b> are particularly vulnerable.  
Easy <b>availability</b> of <b>pornography</b> for <b>children</b> on the 
<b>internet</b> has been an <b>issue</b> worth </i>worrying<i>. A <b>lot</b> of 
online <b>pornography</b> is violent. Frequent <b>exposure</b> to 
<b>pornography</b> may </i>lead<i> to <b>normalization</b> of <b>rape</b>, risky 
sexual <b>behavior</b>, or <b>sex</b> at a young <b>age</b> among other 
<b>effects</b>. The easy <b>availability</b> of <b>pornography</b> is </i>creating<i> 
a dangerous <b>situation</b> where <b>kids</b> get </i>caught<i> up in 
sexually addictive <b>behavior</b> at an early <b>age</b>. Mental 
<b>health</b> <b>professionals</b> are fearful of the <b>impact</b> on future 
<b>generations</b>, </i>comparing<i> <b>internet</b> <b>pornography</b> to “</i>crack<i> 
<b>cocaine</b>” because of its highly addictive <b>nature</b> [3]. 
2 Banning from <b>countries</b>, <b>search</b> 
<b>engines</b>, and social <b>media</b> 2
MATEC Web of Conferences 201, 04004 (2018) https://doi.org/10.1051/matecconf/201820104004
ICI 2017
 
The first <b>defense</b> against <b>child</b> <b>exposure</b> to <b>pornography</b> 
and <b>exploitation</b> is to </i>use<i> a good <b>internet</b> <b>filter</b>, or 
</i>subscribe<i> to a </i>filtered<i> <b>internet</b> <b>service</b>. The <b>internet</b> 
<b>regulation</b> has </i>relied<i> on the <b>system</b> of <b>user</b> <b>reporting</b>, a 
“</i>notify<i> and </i>take<i> down” <b>basis</b>, to </i>tackle<i> the <b>problem</b> of 
online <b>porn</b>. In the United Kingdom the <b>blacklist</b> is open 
and available through <b>institutions</b> such as Internet Watch 
Foundation. 
To better </i>crack<i> down on online <b>pornography</b> and 
</i>make<i> the <b>internet</b> safer for <b>children</b>, <b>internet</b> <b>service</b> 
<b>providers</b> in Britain were </i>asked<i> to </i>make<i> “<b>family</b>-friendly 
<b>filters</b>,” which </i>block<i> <b>X</b>-</i>rated<i> <b>websites</b>, the <b>default</b> for 
<b>customers</b> </i>starting<i> from 2013, because <b>kids</b> are </i>exposed<i> 
to <b>pornography</b> at a young <b>age</b>. Instead of </i>letting<i> <b>people</b> 
</i>choose<i> what </i>filtering<i> they </i>want<i>, the "Yes" <b>option</b> for 
<b>filtering</b> was </i>pre<i></i>-<i></i>ticked<i>. However, the <b>policy</b> was been 
</i>challenged<i> over its <b>censorship</b>. <b>Studies</b> of <b>filters</b> on some 
UK <b>ISPs</b> have </i>shown<i> that well-</i>known<i> <b>porn</b> <b>sites</b> </i>go<i> 
unblocked while <b>education</b> <b>sites</b> about sexually 
</i>transmitted<i> <b>diseases</b> or sexual <b>health</b> are inaccessible [4]. 
At the same <b>time</b>, <b>ISPs</b> and <b>search</b> <b>engines</b> were 
under the <b>pressure</b> from the <b>advocacy</b> <b>groups</b> to </i>tackle<i> 
illegal <b>pornography</b>. Google </i>changed<i> its <b>advertising</b> 
<b>policy</b> in March 2014 to </i>ban<i> pornographic <b>ads</b> from its 
<b>search</b> <b>engine</b>, </i>including<i> <b>ads</b> </i>promoting<i> underage and 
non-consensual sexual <b>content</b>, as well as <b>prostitution</b> 
and <b>escort</b> <b>services</b>. 
Facebook </i>restricts<i> the <b>display</b> of <b>nudity</b> and sexual 
<b>activity</b> because of their <b>audiences</b> cultural <b>background</b> 
or <b>age</b>. <b>Machine</b> <b>learning</b> is </i>used<i> to </i>see<i> if something in a 
<b>photo</b> </i>violates<i> the <b>company</b>'s "Community Standards." 
The social <b>media</b> </i>gave<i> <b>people</b> the <b>option</b> to </i>block<i> </i>mature<i> 
and suggestive <b>content</b> from their <b>News</b> <b>Feeds</b> from 
August in 2016. 
Although YouTube </i>has<i> <b>systems</b> in <b>place</b> to </i>take<i> swift 
<b>action</b> on obscene <b>material</b> both through <b>machine</b> 
<b>learning</b> and by </i>increasing<i> human and technical 
<b>resources</b>, a BBC Trending <b>investigation</b> has </i>discovered<i> 
a <b>flaw</b> in a <b>tool</b> that </i>enables<i> the <b>public</b> to </i>report<i> <b>abuse</b>. 
<b>Part</b> of YouTube's <b>system</b> for </i>reporting<i> </i>sexualized<i> 
<b>comments</b> </i>left<i> on <b>children</b>'s <b>videos</b> has not been 
</i>functioning<i> correctly for more than a <b>year</b> [5]. 
 
3 </i>Fighting<i> back from the <b>porn</b> <b>industry</b> 
After the <b>banning</b> of pornographic <b>ads</b> and </i>blocking<i> 
mature <b>contents</b>, <b>porn</b> <b>industries</b> </i>tried<i> to </i>utilize<i> key 
<b>influencers</b> and </i>embedded<i> <b>marketing</b> in which <b>references</b> 
to <b>porn</b> <b>websites</b> or <b>videos</b> are </i>incorporated<i> into another 
<b>work</b>, such as a <b>newspaper</b> or <b>television</b> <b>news</b>, with a 
specific <b>intent</b> to </i>promote<i> <b>porn</b> <b>websites</b> or <b>videos</b>. <b>Event</b> 
<b>marketing</b> is </i>entering<i> a <b>guerrilla</b> <b>era</b> where the physical 
and the virtual <b>cross</b> <b>paths</b>, </i>offering<i> new <b>options</b> for 
<b>marketing</b> <b>professionals</b> who </i>create<i> <b>buzz</b> over a <b>service</b> 
or <b>product</b>. The </i>created<i> <b>event</b> is </i>called<i> <b>pseudo</b><b>-</b><b>event</b> in 
<b>journalism</b>. For <b>example</b>, the <b>porn</b> <b>industry</b> might </i>create<i> 
a seemingly newsworthy <b>information</b> to </i>distribute<i> a 
<b>news</b>, like an Irish <b>reporter</b> </i>discovered<i> the <b>secret</b> to </i>use<i> 
the <b>keyword</b> of “scannáin” being able to </i>search<i> for a <b>lot</b> 
of </i>hidden<i> pornographic <b>videos</b> on the YouTube [6]. 
 
 
<b>Fig</b>. 1. Google <b>search</b> <b>result</b>. This is a <b>figure</b> </i>showing<i> how the 
<b>news</b> was </i>reported<i> not in 2015 but also till 2018. 
The <b>news</b> would then be </i>reported<i> all over the <b>world</b> 
to </i>give<i> <b>information</b> to <b>people</b>, even <b>children</b>, how to </i>find<i> 
<b>pornography</b> and </i>come<i> along with other true <b>news</b> again 
and again like the <b>hotnews</b> below (Figs. 2 & 3). Even in 
2018, YouTubers will </i>stumble<i> upon what is really porn 
when </i>searching<i> for the <b>keyword</b> “<b>scannán</b>.” 
 
Fig. 2. <b>Type</b> of <b>product</b> <b>placement</b>. This is a <b>figure</b> </i>showing<i> 
how the <b>porn</b> </i>sponsored<i> <b>news</b> repeatedly </i>appears<i> on the 
<b>webnews</b> of a mainstream <b>newspaper</b> of Taiwan in 2018. 
 
Fig. 3. <b>Type</b> of <b>product</b> <b>placement</b>. This is a <b>figure</b> </i>showing<i> 
how <b>porn</b> </i>promoted<i> <b>stories</b> repeatedly </i>appears<i> on the <b>webnews</b> 
of a mainstream <b>newspaper</b> of Taiwan in 2018. 
<b>Porn</b> fake <b>news</b> is </i>produced<i> purposefully to </i>click<i>, 
<b>share</b>, </i>react<i>, and <b>comment</b> just like political fake <b>news</b>. 
Unlike a political fake <b>news</b> </i>aiming<i> to </i>disrupt<i> an <b>election</b> 
or </i>provoke<i> civil <b>unrest</b>, <b>porn</b> fake <b>news</b> is not an <b>issue</b> of 3
MATEC Web of Conferences 201, 04004 (2018) https://doi.org/10.1051/matecconf/201820104004
ICI 2017
 
what <b>news</b> <b>sources</b> to </i>trust<i> or whether the <b>information</b> is 
accurate or not. It is an <b>event</b> <b>marketing</b> by interactively 
</i>hiring<i> online key <b>influencers</b> to </i>create<i> fictional or <b>makeup</b>
<b>news</b> <b>stories</b> with </i>clickbaiting<i> <b>headlines</b> </i>geared<i> to 
</i>travel<i> on social <b>media</b> to </i>click<i> on and </i>share<i> as 
<b>propaganda</b>, which is </i>spread<i> even more widely by 
<b>placement</b> <b>marketing</b> of <b>newspaper</b> and <b>television</b> <b>news</b> 
<b>broadcasting</b> and will </i>last<i> long after the <b>reporting</b> by <b>way</b> 
of <b>PR</b> <b>promotion</b> as <b>advertising</b> (</i>sponsored<i> <b>news</b> you 
may </i>like<i>) to </i>come<i> along with other true <b>news</b> again and 
again to be </i>clicked<i> and to </i>promote<i> their <b>porn</b> <b>websites</b> or 
<b>videos</b> in the <b>nature</b>. 
 
Fig. 4. <b>Type</b> of <b>product</b> <b>placement</b>. This is a <b>figure</b> </i>showing<i> 
how <b>porn</b> fake <b>news</b> </i>appears<i> on the <b>webnews</b> of a mainstream 
<b>newspaper</b> of Taiwan in 2018 without </i>marking<i> as </i>promoted<i>. 
To </i>overcome<i> the <b>issue</b> of <b>age</b>-appropriateness and 
general <b>decency</b>, the <b>pictures</b> are carefully </i>processed<i>, as 
above, not to </i>reach<i> the <b>level</b> of <b>obscenity</b> or sexually 
explicit, so that <b>volunteer</b> <b>moderators</b> can not </i>report<i> it to 
the regulative <b>body</b>. PornHub is especially good at 
</i>making<i> <b>porn</b> fake <b>news</b> without </i>violating<i> ageappropriateness
and general <b>decency</b>. It </i>launched<i> its first 
US <b>advertising</b> <b>campaign</b>, a </i>crowdsourcing<i> <b>competition</b> 
to </i>require<i> <b>entrants</b> to </i>submit<i> a <b>G</b>-</i>rated<i>, suitable for <b>work</b> 
<b>ad</b> (<b>print</b> or <b>multimedia</b>) that clearly </i>promotes<i> the <b>brand</b> 
in 2014. The <b>event</b> </i>received<i> worldwide <b>broadcasting</b> and 
<b>publication</b>, and the </i>winning<i> <b>advertising</b> then was widely 
</i>spread<i> out in <b>news</b> and </i>shared<i> among social <b>media</b> on 
Christmas. 
Hence, a particular <b>event</b> </i>coming<i> from a legitimate 
<b>site</b> of <b>news</b> <b>sources</b> cannot </i>guarantee<i> the <b>event</b> is not a 
<b>porn</b> fake <b>news</b>. For <b>example</b>, CNBC had </i>aired<i> <b>specials</b> 
on <b>prostitution</b> and a <b>documentary</b> </i>called<i> “<b>Porn</b>: 
Business of Pleasure.” <b>Viewers</b> can </i>see<i> a pornographic 
<b>product</b> <b>placement</b> on <b>TV</b> and <b>newspaper</b>’s <b>interviews</b> 
with a <b>series</b> of <b>porn</b>-<b>makers</b> or <b>porn</b> <b>star</b> [7]. 
<b>Production</b> of the fake <b>news</b> is to </i>spread<i> out the 
<b>information</b> about a <b>porn</b> <b>website</b>, <b>prostitution</b>, <b>porn</b> 
</i>related<i> <b>services</b>, <b>videos</b> or <b>products</b> to </i>attract<i> maximum 
<b>attention</b> of <b>people</b>. </i>According<i> to Pornhub, nearly 92 
billion <b>videos</b> were </i>watched<i> over the <b>course</b> of 23 billion 
<b>visits</b> to the <b>site</b> by many <b>millions</b> of very horny <b>visitors</b> 
in 2016. That's 64 million <b>visitors</b> per <b>day</b>, or 44,000 
every <b>minute</b>. 
4 How AI and <b>machine</b> <b>learning</b> <b>fight</b> 
fake <b>news</b>. 
After </i>coming<i> under heavy public <b>criticism</b> for not </i>taking<i> 
full <b>responsibility</b> for fake <b>news</b> </i>affecting<i> the <b>outcome</b> of 
the 2016 presidential <b>election</b>, the <b>technology</b> <b>tycoons</b> 
such as Google, Facebook, and Twitter now </i>plan<i> to 
</i>crack<i> down on fake <b>news</b>. There </i>are<i> four <b>ways</b> 
commonly </i>used<i> by AI and <b>machine</b> </i>learning<i> [8]: 
 
1. <b>Score</b> <b>Web</b> <b>Pages</b>: Google </i>takes<i> the <b>accuracy</b> of <b>facts</b> 
</i>presented<i> to </i>score<i> <b>web</b> <b>pages</b>. The <b>technology</b> has </i>grown<i> 
in <b>significance</b> as it </i>makes<i> an <b>attempt</b> to </i>understand<i> 
<b>pages</b>’ <b>context</b> without </i>relying<i> on third-<b>party</b> <b>signals</b>. 
2. <b>Weigh</b> <b>Facts</b>: A Natural Language <b>Processing</b> <b>engine</b> 
can </i>go<i> through the <b>subject</b> of a <b>story</b> along with the 
<b>headline</b>, main <b>body</b> <b>text</b>, and the <b>geo</b>-<b>location</b>. Further, 
artificial <b>intelligence</b> will </i>find<i> out if other <b>sites</b> are 
</i>reporting<i> the same <b>facts</b>. In this <b>way</b>, <b>facts</b> are </i>weighed<i> 
against reputed <b>media</b> <b>sources</b>. 
3. </i>Predict<i> <b>Reputation</b>: </i>Using<i> predictive <b>analytics</b> </i>backed<i> 
by Machine Learning, a <b>website</b>’s <b>reputation</b> can be 
</i>predicted<i> through </i>considering<i> multiple <b>features</b> like 
<b>domain</b> <b>name</b> and Alexa <b>web</b> <b>rank</b>. 
4. Discover Sensational Words: When it </i>comes<i> to <b>news</b> 
<b>items</b>, the <b>headline</b> is the <b>key</b> to </i>capturing<i> the <b>attention</b> 
of the <b>audience</b>. Artificial Intelligence has been 
instrumental in </i>discovering<i> and </i>flagging<i> fake <b>news</b> 
<b>headlines</b> by </i>using<i> <b>keyword</b> <b>analytics</b>. 
 
These might be <b>ways</b> to </i>combat<i> political fake <b>news</b>, 
but they are not good <b>ways</b> to </i>mitigate<i> the <b>damage</b> 
</i>caused<i> by <b>porn</b> fake <b>news</b> for <b>children</b>. 
AI <b>systems</b> are </i>used<i> to </i>fill<i> the <b>gaps</b> </i>left<i> by online 
<b>fact</b>-</i>checking<i> <b>outlets</b>, whose human <b>fact</b>-</i>checkers<i> <b>lack</b> 
the <b>bandwidth</b> to </i>evaluate<i> every <b>article</b> that </i>appears<i> 
online. </i>Designing<i> a fully </i>automated<i> fake <b>news</b> <b>detector</b> 
is currently infeasible, because the <b>problem</b> at <b>hand</b> is 
too complex for <b>technology</b> alone. 
There </i>are<i> many different <b>categories</b> <b>misinformation</b> 
can </i>fall<i> into. Even the <b>subproblem</b> of </i>defining<i> the 
<b>criteria</b> under which to </i>classify<i> <b>news</b> as “fake” </i>creates<i> 
<b>ambiguity</b> that </i>requires<i> human <b>judgment</b>. The <b>ability</b> to 
</i>determine<i> whether an <b>article</b> is real or fake </i>requires<i> more 
than just <b>information</b> about the <b>article</b>; it </i>requires<i> an 
<b>understanding</b> of cultural <b>factors</b>, for <b>example</b> “<b>tea</b>” 
maybe </i>used<i> by <b>prostitution</b> and <b>escort</b> <b>services</b> in Taiwan, 
and “John” is <b>prostitute</b>'s <b>client</b> in US <b>slang</b>. Algorithms 
will be helpful, but real <b>progress</b> on <b>understanding</b> or 
</i>controlling<i> the fake <b>news</b> <b>phenomenon</b> is ultimately 
about <b>humans</b> not <b>machines</b>. Current <b>forms</b> of AI can 
</i>look<i> at the <b>style</b> of the <b>language</b>, and the <b>topic</b> that the 
<b>text</b> is </i>discussing<i>, but it can’t </i>figure<i> out the <b>meaning</b> 
behind <b>statements</b> [9]. 
Even though an AI-</i>based<i> <b>system</b> like Enterra would 
be able to </i>interpret<i> the <b>phrase</b> "</i>seeing<i> red" in <b>context</b> as 
</i>referring<i> to a high <b>level</b> of <b>frustration</b>, because it can 
</i>perform<i> <b>human</b>-like <b>reasoning</b> and </i>analyze<i> the <b>report</b> 4
MATEC Web of Conferences 201, 04004 (2018) https://doi.org/10.1051/matecconf/201820104004
ICI 2017
 
contextually [10], it might not be able to </i>detect<i> the 
fraudulent <b>stories</b> </i>disguised<i> in the <b>form</b> of <b>product</b> 
<b>placement</b> in <b>journalism</b>. 
The <b>way</b> that Facebook <b>polices</b> </i>mature<i> <b>content</b> is 
</i>using<i> AI to </i>monitor<i> <b>video</b> on Facebook Live and </i>flag<i> it, 
if offensive <b>content</b> is </i>found<i>. But the <b>study</b> doesn’t 
</i>recommend<i> the <b>machine</b> </i>learning<i> to </i>make<i> a <b>model</b> to 
</i>flag<i> <b>news</b> <b>content</b> as <b>porn</b> fake <b>news</b>. </i>Using<i> a red <b>banner</b> 
to </i>highlight<i> that a <b>story</b> is fake to </i>prevent<i> it </i>going<i> viral is 
even worse for </i>decreasing<i> <b>children</b>’s <b>accessibility</b> to 
<b>porn</b> fake <b>news</b> by </i>alerting<i> their <b>attention</b>. 
</i>Trying<i> to </i>predict<i> whether a <b>news</b> <b>site</b> is a fake <b>news</b> 
<b>site</b> or not is one possible <b>way</b> to </i>solve<i> the <b>porn</b> fake 
<b>news</b> <b>problem</b> if these <b>stories</b> </i>come<i> from the <b>bloggers</b> or 
key <b>influencers</b> of social <b>media</b> who constantly </i>produce<i> 
<b>porn</b> fake <b>news</b>. But this <b>way</b> is not realistic for the <b>porn</b> 
fake <b>news</b> </i>produced<i> as an <b>event</b> <b>marketing</b> by the <b>porn</b> 
<b>industry</b> on the <b>mainstream</b> <b>media</b>. 
The <b>study</b> </i>suggests<i> one <b>way</b> to </i>solve<i> the <b>problem</b>: 
beyond </i>predicting<i> a <b>website</b>’s <b>reputation</b> and </i>discovering<i> 
sensational <b>words</b>, <b>researchers</b> </i>need<i> to </i>create<i> a <b>database</b> 
</i>according<i> to cultural <b>codes</b> and to </i>use<i> a Natural 
<b>Language</b> <b>Processing</b> <b>engine</b> to </i>go<i> through the <b>message</b> 
to </i>find<i> the <b>websites</b> or the <b>keywords</b> </i>mentioned<i> in the 
<b>news</b>, and then to </i>follow<i> and </i>check<i> the <b>websites</b> or the 
<b>keywords</b>. If they </i>lead<i> to an <b>age</b>-<b>verification</b> <b>sign</b> like 
Fig. 5 or obscene <b>pictures</b> or <b>videos</b>, then they must be a 
<b>news</b> to be </i>filtered<i> away from <b>children</b>. 
 
Fig. 5. <b>Age</b>-<b>verification</b> <b>sign</b>. This is a <b>figure</b> </i>showing<i> that an 
<b>age</b>-<b>verification</b> <b>sign</b> </i>used<i> in Taiwan, which can be easily 
</i>cheated<i> by <b>children</b> under 18 <b>years</b> old to </i>click<i> the “I</i>’m<i> over 
18 <b>years</b> old” <b>button</b> and </i>pass<i> <b>age</b>-<b>verification</b>. 
5 <b>Conclusions</b> 
The <b>study</b> </i>points<i> to a <b>fact</b> which </i>needs<i> equal <b>attention</b> 
when the <b>world</b> is </i>focusing<i> on the political fake <b>news</b> 
after the 2016 US presidential <b>election</b>. That is <b>porn</b> fake 
<b>news</b> which </i>has<i> much <b>impact</b> on <b>children</b>. To </i>protect<i> 
<b>children</b> from </i>viewing<i> inappropriate <b>adult</b> <b>material</b>, 
United Kingdom is </i>going<i> to </i>activate<i> the Age 
Verification for Online Pornography (<b>clauses</b> 15-25) on 
the Digital Economy Bill from 2018, which </i>asks<i> anyone 
who </i>makes<i> <b>pornography</b> available online on a 
commercial <b>basis</b> must </i>ensure<i> under <b>18s</b> in the UK 
cannot </i>access<i> it. If <b>machine</b> <b>learning</b> can </i>do<i> a better <b>job</b> 
to </i>combat<i> the <b>war</b> by </i>building<i> a better <b>family</b>-friendly 
<b>filter</b>, <b>government</b> <b>regulation</b> can be loosen. The 
<b>researcher</b> </i>observed<i> different <b>types</b> of <b>porn</b> fake <b>news</b> 
and how they </i>appear<i> on different <b>media</b> to </i>spread<i>. These 
<b>observations</b> might </i>provide<i> <b>researchers</b> in <b>machine</b> 
<b>learning</b> or other AI <b>tools</b> some <b>thoughts</b> to </i>build<i> a more 
useful <b>model</b> to </i>mitigate<i> the <b>danger</b> of <b>porn</b> fake <b>news</b> to 
<b>children</b>. 
<b>References</b> 
1. P. Perry, Available online:  
<b>http://bigthink.com/philip-perry/these-ai-toolscould-lead-to-the-next-generation-of-fake-news</b>
(</i>accessed<i> on 2017). 
2. L. Gilkerson, Available online: 
http://www.covenanteyes.com/2013/02/19/pornogra
<b>phy</b>-<b>statistics/</b> (</i>accessed<i> on 22 Sep. 2013). 
3. Available online:  
<b>http://coheargroup.com/services/sexual-recoveryservices/pornography-addiction-in-adolescents/</b>
(</i>accessed<i> on 2017). 
4. Available online:   
http://www.bbc.com/news/technology-23403068 
(</i>accessed<i> on 2017). 
5. BBC, Available online:  
http://citifmonline.com/2017/11/24/flaw-youtubesobscenity-tracking-tool/
(</i>accessed<i> on 2017). 
6. T. Lee, Available online:  
http://www.ubergizmo.com/2015/02/porn-uploadedand-disguised-on-youtube-using-irish-language-
titles/ (</i>accessed<i> on 2017). 
7. CNBC Available online:   
</i>https://www.mrc.org/articles/cnbc-mainstreamsgross-out-porn<i>
(</i>accessed<i> on 2017). 
8. R. Akiwatkar, Available <b>online</b>: 
https://channels.theinnovationenterprise.com/articles
/how-can-artificial-<b>intelligence</b>-<b>combat</b>-fake-<b>news</b> 
(</i>accessed<i> on 2017). 
9. Available online:  https://towardsdatascience.com/itrained-fake-news-detection-ai-with-95-accuracy-
and-almost-</i>went<i>-crazy-</i>d10589aa57c<i> (</i>accessed<i> on 
2017). 
10. <b>A.</b> Wolk, Available online:   
https://www.forbes.com/sites/alanwolk/2018/01/17/
can-<b>enterras</b>-</i>advanced<i>-<b>ai</b>-<b>systems</b>-</i>stop<i>-the-<b>fakenews</b>-epidemic/#6d264af92049
(</i>accessed<i> on 2018). 