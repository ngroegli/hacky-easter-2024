import re

root_two_back = "4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727350138462309122970249248360558507372126441214970999358314132226659275055927557999505011527820605714701095599716059702745345968620147285174186408891986095523292304843087143214508397626036279952514079896872533965463318088296406206152583523950547457502877599617298355752203375318570113543746034084988471603868999706990048150305440277903164542478230684929369186215805784631115966687130130156185689872372352885092648612494977154218334204285686060146824720771435854874155657069677653720226485447015858801620758474922657226002085584466521458398893944370926591800311388246468157082630100594858704003186480342194897278290641045072636881313739855256117322040245091227700226941127573627280495738108967504018369868368450725799364729060762996941380475654823728997180326802474420629269124859052181004459842150591120249441341728531478105803603371077309182869314710171111683916581726889419758716582152128229518488472089694633862891562882765952635140542267653239694617511291602408715510135150455381287560052631468017127402653969470240300517495318862925631385188163478001569369176881852378684052287837629389214300655869568685964595155501644724509836896036887323114389415576651040883914292338113206052433629485317049915771756228549741438999188021762430965206564211827316726257539594717255934637238632261482742622208671155839599926521176252698917540988159348640083457085181472231814204070426509056532333398436457865796796519267292399875366617215982578860263363617827495994219403777753681426217738799194551397231274066898329989895386728822856378697749662519966583525776198939322845344735694794962952168891485492538904755828834526096524096542889394538646625744927556381964410316979833061852019379384940057156333720548068540575867999670121372239475821426306585132217408832382947287617393647467837431960001592188807347857617252211867490424977366929207311096369721608933708661156734585334833295254675851644710757848602463600834449114818587655554286455123314219926311332517970608436559704352856410087918500760361009159465670676883605571740076756905096136719401324935605240185999105062108163597726431380605467010293569971042425105781749531057255934984451126922780344913506637568747760283162829605532422426957534529028838768446429173282770888318087025339852338122749990812371892540726475367850304821591801886167108972869229201197599880703818543332536460211082299279293072871780799888099176741774108983060800326311816427988231171543638696617029999341616148786860180455055539869131151860103863753250045581860448040750241195184305674533683613674597374423988553285179308960373898915173195874134428817842125021916951875593444387396189314549999906107587049090260883517636224749757858858368037457931157339802099986622186949922595913276423619410592100328026149874566599688874067956167391859572888642473463585886864496822386006983352642799056283165613913942557649062065186021647263033362975075697870606606856498160092718709292153132368281356988937097416504474590960537472796524477094099241238710614470543986743647338477454819100872886222149589529591187892149179833981083788278153065562315810360648675873036014502273208829351341387227684176678436905294286984908384557445794095986260742499549168028530773989382960362133539875320509199893607513906444495768456993471276364507163279154701597733548638939423257277540038260274785674172580951416307159597849818009443560379390985590168272154034581581521004936662953448827107292396602321638238266612626830502572781169451035379371568823365932297823192986064679789864092085609558142614363631004615594332550474493975933999125419532300932175304476533964706627611661753518754646209676345587386164880198848497479264045065444896910040794211816925796857563784881498986416854994916357614484047021033989215342377037233353115645944389703653166721949049351882905806307401346862641672470110653463493916407146285567980177933814424045269137066609777638784866238003392324370474115331872531906019165996455381157888413808433232105337674618121780142960928324113627525408873729051294073394794330619439569367020794295158782283493219316664111301549594698378977674344435393377099571349884078908508158923660700886581054709497904657229888808924612828160131337010290802909997456478495815456146487155163905024198579061310934587833062002622073724716766854554999049940857108099257599288932366154382719550057816251330381531465779079268685008069844284791524242754410268057563215653220618857512251130639370253629271619682512591920252160587011895967322442392674237344907646467273753479645988191498079317180024238554538860383683108007791824664627541174442500187277795181643834514634612990207633430179685543856316677235183893366670422221109391449302879638128398893117313084300421255501854985065294556377660314612559091046113847682823595924772286290426427361632645854433928772638603431498048963973633297548859256811492968361267258985738332164366634870234773026101061305072986115341299488087744731112295426527516536659117301423606265258690771982170370981046443604772267392829874152593069562063847108274082184906737233058743029709242899481739244078693752844010443990485208788519141935415129006817351703069386970590047425157655248078447362144105016200845444122255956202984725940352801906798068098300396453985685930458625260637797453559927747299064888745451242496076378010863900191058092874764720751109238605950195432281602088796215162338521612875228518025292876183257037172857406763944909825464422184654308806610580201584728406712630254593798906508168571371656685941300533197036596403376674146104956376510308366134893109478026812935573318905519705201845150399690986631525124116111925940552808564989319589834562331983683494880806171562439112866312797848371978953369015277600549805516635019785557110140555297633841275044686046476631832661165182067501204766991098721910444744032689436415959427921994423553718704299559240314091712848158543866005385713583639816309452407557009325168243441682408361979273372825215462246961533217026829950979089034594858878349439616204358422497397187113958927305092197054917176961600445580899427878880369169432894595147226722926124850696173163809410821860045286102696547576304310256027152313969482135519821409716549097319992834925674097490392297126348693414574933198041718076111963902278664075922434167762466236238913110270343304576368141128321326308582239456219598086612939996201234156176318174312420089014983848560480879864608393596492366514296812577314322914568716827621996118278269531574983802624651759054103976181287604216386134502213262727756612441133610775195557749508656360673786650623185640699122801875741785494661253275997697960597760590756489106661015838417202818530432119044657752554277543798726054881736198267581686283295260789932226683602838513512281059318591028641508157056319717315183136250243590414632122392176633982689368253150530059891547029095371932662073411234947433678846902013904978428521634144292145895582878476693946464267812219049785636355263368278051860098699248937786002398769169807656621943898544370805946433362333810587458162354756001365924352426571430834655457680023708146757325254702550747637471635067851599173693793251032682760628645914618204721486370370771926926823623334720379245964691810526139153086280291440965482563873092730426544662929045896063751918711469345361973324789572707031530930901921199199993615765003503984054067425387927527922724733566770607837911384488936261367657060263600315132952095395202854897384486256134924414708607086602676349978793420875836121947116994223848482595914304528107062601508969135303017720062717054402090669514915274597719705947695474095210287872557856880022193717743558110793930883384558648277291008629554566141306721230848740227121058686323388237413884428938155444647105755651468435702946635062893873569868688376480326519528414653517395302736120137420300986739838514321900436028982698293529399414129230580384565022707216815161941011449826301364900877048398488386090653368599054583895203185648041493272142390865164999431659207965953569430723112911629286797517156688905439322035691293324570208067194440497304943981408227829602799424541083166675921424835182723817205041039274288801556223380796147512433514731021284545944899444996000752437519570116683417447490795882099517836768023236517674972301487457742725994760962198432714835298611190272873584905217975908374197486026706053746231530039375212367867752848692195857137554269684827836317861109933680143915905974842858054516130230143979057016108898627779610750673332676048654929251399781390535882276893732204941483940135560356560442140176120605131806891989962606184831853401836237821726637580455247196266174925422852804571442048578342113228008528704205488992341278554812367615377071042544698685219911228354266349997127483660762462418207364666171283947484732804744304033441072004287271275670279567582429262719454580530026664899650795697781786219421720052371653694677041951119127046248360511302890464377511486948878496151188414719100012558838366606772084112351535588112677895715585904125762616010675131535802124273318710006358249545040995794072547989003168265123731190556682915194305370848930786919742829049038603723116099283424317122250994547150192866648787107951995180054633883844315481724635480244518030845273431000621371034625733060012349737443558180965678464641533905146569193245623531405779193698988423647183525375805257713311200797104068315492665402026046806818391437827214769063242469517128636738443139833371176159418699934662623453734523567940124168092291163609563721674528391709909146648507392051516056047378710615470216996074656930979442612146925615934256494019122989514732544715181263258368897282262833295240359700727863364604594707124174729468775705958157349962848099567839255474240448991887071069675242507745201229360810574142653234724064162141033353340551104521261750359028403745459186450472762434207177092979354010214096464502836834180407586081001407216192477179809859681115404464437285689592868319777977869346415984697451339177415379048778808300220583350467465553230285873258351"




def solve_dynamic_rot_with_ascii(cipher, key):
    if(len(key) != len(cipher)):
        print("The key (length {0}) and cipher (length{1}) have to be same long!", len(key), len(cipher))
        return

    index = 0
    result = ""
    for c in cipher:
        plaintext_char = chr(ord(c) - int(key[index]))
        result = result + plaintext_char
        index = index + 1

    print("Flag:     {0}".format(result)) # he2024{That_wa5_a_b1t_1rrat10nal_but_0kaaay.}


def find_all_matches(pattern, string):
    pat = re.compile(pattern)
    pos = 0
    out = []
    while (match := pat.search(string, pos)) is not None:
        pos = match.start() + 1
        out.append(match[1])
    return out



if __name__ == "__main__":
    # solve_rot_with_ascii_and_pi()
    root_two = "414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572735013846230912297024924836055850737212644121497099935831413222665927505592755799950501152782060571470109559971605970274534596862014728517418640889198609552329230484308714321450839762603627995251407989687253396546331808829640620615258352395054745750287759961729835575220337531857011354374603408498847160386899970699004815030544027790316454247823068492936918621580578463111596668713013015618568987237235288509264861249497715421833420428568606014682472077143585487415565706967765372022"
    
    pi = "14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999837297804995105973173281609631859502445945534690830264252230825334468503526193118817101000313783875288658753320838142061717766914730359825349042875546873115956286388235378759375195778185778053217122680661300192787661119590921642019893809525720106548586327886593615338182796823030195203530185296899577362259941389124972177528347913151557485724245415069595082953311686172785588907509838175463746493931"
    
    e = "7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424371075390777449920695517027618386062613313845830007520449338265602976067371132007093287091274437470472306969772093101416928368190255151086574637721112523897844250569536967707854499699679468644549059879316368892300987931277361782154249992295763514822082698951936680331825288693984964651058209392398294887933203625094431173012381970684161403970198376793206832823764648042953118023287825098194558153017567173613320698112509961818815930416903515988885193458072738667385894228792284998920868058257492796104841984443634632449684875602336248270419786232090021609902353043699418491463140934317381436405"

    key_values = find_all_matches(r'41(\d)', root_two)
    key = ""
    counter = 0
    for k in key_values:
        if counter == 54:
            break
        key = key + k
        counter = counter + 1
    
    cipher = "he876:|I94kcxk6uohyp9t4cn}ti:vtcir7foowg8tbk8sfy~4166~"
    print("Reversing ...")
    print("Cipher:   {0}".format(cipher))
    print("Key:      {0}".format(key))
    print("Expected: he2024{                                              }")
    solve_dynamic_rot_with_ascii(cipher, key)