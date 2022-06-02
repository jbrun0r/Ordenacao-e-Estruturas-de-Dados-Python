{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ArvorePATRICIA_Bruno.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jbrun0r/Ordenacao-e-Estruturas-de-Dados-Python/blob/main/ArvorePATRICIA_Bruno.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dGG8V3vuKZin"
      },
      "source": [
        "JOÃO BRUNO RODRIGUES DE FREITAS\n",
        "ARVORE PATRICIA"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RUrjU8KrKnFl"
      },
      "source": [
        "##ARVORE PATRICIA\n",
        "\n",
        "from collections import defaultdict\n",
        "\n",
        "class Patricia():\n",
        "    def __init__(self,eh_palavra=False,chaves=None):\n",
        "        self.eh_palavra = eh_palavra\n",
        "        self.children=chaves if chaves else defaultdict(Patricia)\n",
        "\n",
        "class Trie():\n",
        "    def __init__(self):\n",
        "        self.raiz=Patricia()\n",
        "\n",
        "    def insere(self, palavra):\n",
        "        return self.aux(self.raiz, palavra)\n",
        "\n",
        "    def aux(self, no, palavra):\n",
        "        for chave,child in no.children.items():\n",
        "            prefixo, divide, rest = self.inicio(chave, palavra)\n",
        "            if not divide:\n",
        "                if not rest:\n",
        "                    child.eh_palavra=True\n",
        "                    return True\n",
        "                else:\n",
        "                    return self.aux(child, rest)\n",
        "            if prefixo:\n",
        "                novo_no=Patricia(eh_palavra=not rest,chaves={divide:child})\n",
        "                no.children[prefixo]=novo_no\n",
        "                del no.children[chave]\n",
        "                return self.aux(novo_no, rest)\n",
        "        no.children[palavra]=Patricia(eh_palavra=True)\n",
        "\n",
        "    def busca(self, palavra):\n",
        "        return self.busca_aux(self.raiz,palavra)\n",
        "\n",
        "    def busca_aux(self,no, palavra):\n",
        "        for chave,child in no.children.items():\n",
        "            prefixo, divide, rest = self.inicio(chave, palavra)\n",
        "            if not divide and not rest:\n",
        "                return child.eh_palavra\n",
        "            if not divide:\n",
        "                return self.busca_aux(child,rest)\n",
        "        return False\n",
        "\n",
        "    def comeca(self,palavra):\n",
        "        return self.comeca_com_aux(self.raiz,palavra)\n",
        "\n",
        "    def comeca_com_aux(self,no,palavra):\n",
        "        for chave,child in no.children.items():\n",
        "            prefixo, divide, rest = self.inicio(chave, palavra)\n",
        "            if not rest:\n",
        "                return True\n",
        "            if not divide:\n",
        "                return self.comeca_com_aux(child,rest)\n",
        "        return False\n",
        "\n",
        "    def inicio(self, chave, palavra):\n",
        "        i=0\n",
        "        for k,w in zip(chave,palavra):\n",
        "            if k!=w:\n",
        "                break\n",
        "            i+=1\n",
        "        return chave[:i],chave[i:],palavra[i:]"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
