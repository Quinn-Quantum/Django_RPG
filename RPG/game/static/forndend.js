var eigenleben;
        var gegnerleben;
        var ran;
        var damage;
        var damagemath;

       function startKampf(charLeben, gegnerLeben){
            eigenleben =charLeben;
            gegnerleben =gegnerLeben;

            document.getElementById('Char').style.visibility = 'visible';
            document.getElementById('Gegner').style.visibility = 'visible';
            document.getElementById('Atacken').style.visibility = 'visible';
            document.getElementById('start').style.visibility = 'hidden';
            document.getElementById('leben').innerHTML= 'Leben: '+eigenleben;
            document.getElementById('leben2').innerHTML='Gegner Leben: '+gegnerleben;
       };

      function Kampf(){
            document.getElementById('leben').innerHTML= 'Leben: '+ eigenleben;
            document.getElementById('leben2').innerHTML='Gegner Leben: '+ gegnerleben;


            if (eigenleben <=0 || gegnerleben <=0){
                document.getElementById('Atacken').style.display = "none";
                    if (gegnerleben<= 0){
                        var gut = 'Sie haben gewonnen, herzlichen Glückwunsch'
                        document.getElementById('ausgang').innerHTML=gut;
                        document.getElementById('Sieg').style.visibility = 'visible';
                    }
                    else{
                        var schlecht = 'Sie haben leider verloren.'
                        document.getElementById('ausgang').innerHTML=schlecht;
                        document.getElementById('Niederlage').style.visibility = 'visible';
                    }


            }

    }
    var min = 1;
     function angriffSwerthib(charATK,charLevel,gegnerDEF ){

            document.getElementById('angrif1').disabled = true; //Butten aus
            document.getElementById('angrif2').disabled = true;
            document.getElementById('gegnerk').disabled = false; //Butten an
            random = Math.floor(Math.random() * (charATK - min)) + min;

            if (random <= charATK){
                damagemath=(charATK*((2*charLevel+10)/100)/gegnerDEF)*15
                damage = Math.round(damagemath)
                gegnerleben = gegnerleben - damage;
            }


        }
     function angriffMagieball(charMan,charLevel,gegnerDEF){
            document.getElementById('angrif2').disabled = true;
            document.getElementById('angrif1').disabled = true;
            document.getElementById('gegnerk').disabled = false;
            random = Math.floor(Math.random() * (charMan - min)) + min;

            if (random <= charMan){
                damage=(charMan*(2*charLevel+10/100))/gegnerDEF
                damage = Math.round(damage)
                gegnerleben = gegnerleben - damage;
            }


        }
     function gegnerk(gegnerATK, gegnerMAN,charLevel, charDEF){
            document.getElementById('angrif1').disabled = false;
            document.getElementById('angrif2').disabled = false;
            document.getElementById('gegnerk').disabled = true;

            var wahl =  Math.floor(Math.random()*2)+1
            if (wahl == 1){
                random = Math.floor(Math.random() * (gegnerATK - min)) + min;

                if (random <= gegnerATK){
                damage=(gegnerMAN*(2*charLevel+10/100))/charDEF
                damage = Math.round(damage)
                eigenleben = eigenleben - damage;
                }
            }
            else{
                random = Math.floor(Math.random() * (gegnerMAN - min)) + min;

                if (random <= gegnerMAN){
                damage=(gegnerATK*(2*charLevel+10/100))/charDEF
                damage = Math.round(damage)
                eigenleben = eigenleben - damage;
                }
            }


}