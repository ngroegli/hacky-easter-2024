import math
from Crypto.Util.number import long_to_bytes
from decimal import Decimal
from sympy import symbols, Eq, solve, mod_inverse


def main():
    e = 65537
    d = 108558249913654912965940302330463677659522327849752040249154983537931376711447753446078750459585068929061255563115321514107583357553375511879499468302459674778888941298684123550665943662956973368472434636899177211390575049269298954055740191242891907815891881074808494461835202709340654804790036874512758297194884778457538655665389842207203276000134877032836449478050322547852636564447336587949060158710830910425415789299719726199747636954120947724281386286626712561093374518507186661634721441026468041965091952487426455334066534862315923969845098027755755254715248428307745802890502029004449910036589111577136508145
    h1 = 17061347780794249474937241232210067248853992326832612618246691021883473946134655677687441412157857703606444858129229798729181511999941417079248816916398800254158380205975686822877683332947748593883879973137797066913439129505904185975901786363274357224292820647481353241115812182163209817605574692194107051614650879245007286513127155460653132782119052901592516408114681455884212579226838379050354351979274017290886704282949858854855220545880052711872903284127358620618442660935241175277762438290440049748381402411449900120675924310471041887374487007916064485523648828943063195915214058020064461558868092911435089696088
    h2 = 17061347780794249474937241232210067248853992326832612618246691021883473946134655677687441412157857703606444858129229798729181511999941417079248816916398800254158380205975686822877683332947748593883879973137797066913439129505904185975901786363274357224292820647481353241115812182163209817605574692194107051614682608366033433427655544056745556231593264049326018746703896654050234167841676926759637292807314933999966217282511228601089336295804775690349998659758021221369291834448080631738623473608907605109479463903233113943877434062712654852684276670025876108200973499112716384186485697596614301411957746226430962874694
    c = 14771953974869185325753989999306439169443459281017081802044481705032517760143246701952224108615433676555537192461592401710821963371007536567639647832688058381891594635660859018696254198047688405300791235710434996224199879812976316080274952979341960888489269818275411609645795086978322948402441951067219638588493452491788331610154636140788429371883451252588276364444451828866264706502965568460521644194954212456499395773412419744293595190319748377663678851564473399009986610885340941400903567168569899086596357735279151544561157005272580423383179382044165112576721925333630920881944840019797400553640581402786291466801

    p, q, n = symbols('p q n')

    eq1 = Eq(n - p, h1)
    eq2 = Eq(n - q, h2)

    p, q = symbols('p q')

    eq1 = Eq((p*q) - p, h1)
    eq2 = Eq((p*q) - q, h2)

    solution = solve((eq1, eq2), (p, q))

    # Print the solution p and q
    print("Solution:", solution)
    
    # Positive numbers from solution
    p = 147443556029330606689946721653275418114032787692919491444942244413259965145789401665110780525704081778022633149811632207917008039060831922948969371828393257061434554305621417725302756389359317180783465605467004583616718246713617180713681491500626870483291877419659461682805046577754268428581389858491405718103
    q = 115714435003183692161558125560851968639821639959417152855727046247238376530950853955827839697663165068943120150250262461682892289136108944471873996197730656310585380792781961264441721070891761819685404113683790760415208494472004215403891829390815247805967207250006273411533407001204428575491736543495532539497

    n = p * q

    print("Control-check h1 == n - p: ", h1 == n - p)
    print("Control-check h2 == n - q: ", h2 == n - q)

    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)

    print("Control-check d == pow(e, -1, phi): ", d == pow(e, -1, phi))

    m = symbols('m')
    eq = Eq(pow(c, d, n), m) # Reverse c = pow(m, e, n)

    # Solve for m
    solution = solve(eq, m)

    m = solution[0]

    # Print the solution
    print("m =", m)

    print("Flag =", long_to_bytes(m).decode())


if __name__ == "__main__":
    main()