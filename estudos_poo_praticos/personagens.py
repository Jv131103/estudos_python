class Personagem:
    def __init__(self, nome, hp=100, nivel=1):
        self.nome = nome
        self.hp = hp
        self.hp_max = hp  # ← guarda o máximo para limitar a cura
        self.nivel = nivel

    def status(self):
        print(f"{self.nome} (HP: {self.hp}/{self.hp_max} | Nível: {self.nivel})")


class MagicMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mana = 100

    def lancar_feitico(self, alvo):
        if self.mana < 20:
            print("Mana insuficiente!")
            return
        if alvo.hp <= 0:
            print(f"{alvo.nome} já está morto!")
            return
        if alvo.nivel > self.nivel:
            print("Nível insuficiente para causar dano!")
            return
        self.mana -= 20
        dano = 35
        alvo.hp = max(0, alvo.hp - dano)
        print(f"✨ {self.nome} lança feitiço em {alvo.nome}! {dano} de dano. HP: {alvo.hp}/{alvo.hp_max}")


class WarriorMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stamina = 100

    def golpe_pesado(self, alvo):
        if self.stamina < 25:
            print("Stamina insuficiente!")
            return
        if alvo.hp <= 0:
            print(f"{alvo.nome} já está morto!")
            return
        if alvo.nivel > self.nivel:
            print("Nível insuficiente para causar dano!")
            return
        self.stamina -= 25
        dano = 50
        alvo.hp = max(0, alvo.hp - dano)
        print(f"⚔️  {self.nome} usa Golpe Pesado em {alvo.nome}! {dano} de dano. HP: {alvo.hp}/{alvo.hp_max}")


class HealerMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.energia = 100

    def curar(self, alvo):
        if self.energia < 30:
            print("Energia insuficiente!")
            return
        if alvo.hp <= 0:
            print(f"{alvo.nome} já está morto!")
            return
        self.energia -= 30
        cura = 40
        alvo.hp = min(alvo.hp_max, alvo.hp + cura)  # ← respeita o hp_max
        print(f"❤️  {self.nome} cura {alvo.nome}! +{cura} HP. HP: {alvo.hp}/{alvo.hp_max}")


class Guerreiro(WarriorMixin, Personagem):
    def atacar(self, alvo):
        self.golpe_pesado(alvo)


class Mago(MagicMixin, Personagem):
    def atacar(self, alvo):
        self.lancar_feitico(alvo)


class Paladino(WarriorMixin, HealerMixin, Personagem):
    def atacar(self, alvo):
        self.golpe_pesado(alvo)

    def realizar_cura(self, alvo):
        self.curar(alvo)


class ArcanoBerserker(WarriorMixin, MagicMixin, Personagem):
    def atacar(self, alvo):
        self.golpe_pesado(alvo)
        self.lancar_feitico(alvo)  # ← ataca com os dois de uma vez


# Teste
print("=== STATUS INICIAL ===")
arcanjo = Paladino(nome="Miguel", nivel=100)
soldado = Guerreiro(nome="Godfried", nivel=50)
mago = Mago(nome="Merlin", nivel=80)
berserker = ArcanoBerserker(nome="Ragnar", nivel=70)

arcanjo.status()
soldado.status()

print("\n=== COMBATE ===")
arcanjo.atacar(soldado)
arcanjo.realizar_cura(soldado)  # cura depois de apanhar
arcanjo.atacar(soldado)
arcanjo.atacar(soldado)

print("\n=== ARCANO BERSERKER ===")
berserker.atacar(mago)  # golpe + feitiço no mesmo turno
