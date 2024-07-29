import datetime

import requests

from shinobi.parser.staff import StaffParser
from shinobi.utilities.session import session


def get_staff_res_given_mal_id(mal_id: int) -> requests.Response:
    return session.get(f"https://myanimelist.net/people/{mal_id}")


# noqa: E501
def test_first_person_parser() -> None:
    res = get_staff_res_given_mal_id(1)
    parser = StaffParser(res.text)
    data = parser.build_dictionary()

    assert int(data["mal_id"]) == 1
    assert data["name"] == "Tomokazu Seki"
    assert (
        str(data["staff_image"])
        == "https://cdn.myanimelist.net/images/voiceactors/1/55486.jpg"
    )
    assert data["given_name"] == "智一"
    assert data["family_name"] == "関"
    assert data["alternate_name"] == ["Seki Mondoya", "門戸 開", "Monto Hiraku"]
    assert data["birthday"] == datetime.datetime(1972, 9, 8, 0, 0)

    # assert (
    #     data["about"]
    #     == "Hometown: Tokyo, Japan\nBlood type: AB\n\nTwitter: @seki0908\nProfile: Atomic Monkey"
    # )


# noqa: E501
def test_second_person_parser() -> None:
    res = get_staff_res_given_mal_id(2)
    parser = StaffParser(res.text)
    data = parser.build_dictionary()

    assert data["mal_id"] == 2
    assert data["name"] == "Tomokazu Sugita"
    assert (
        data["staff_image"]
        == "https://cdn.myanimelist.net/images/voiceactors/2/60638.jpg"
    )
    assert data["given_name"] == "智和"
    assert data["family_name"] == "杉田"
    assert data["alternate_name"] == []
    assert data["birthday"] == datetime.datetime(1980, 10, 11, 0, 0)
    # assert (
    #     data["about"]
    #     == "Hometown: Saitama, Japan\nBlood type: B\nHeight: 178 cm\nWeight: 57 kg\n\nTwitter: @sugitaLOV\nStaff Twitter: @AGRS_staff\nStaff Instagram: @agrs_staff\nYouTube: [url=https://www.youtube.com/@agrs5225[/url]"
    # )


# noqa: E501
def test_sora_amamiya() -> None:
    """
    Sora-chan UwU
    It makes sure dat the sora-chan's ID is 21517 and dat dere is an image of hew.
    It also checks the sora-chans's name, birthday, and some other details, like where they're fwom and what dey weigh.
    If all da checks pass, den dis test will pass too!
    Yay !!!
    """
    res = get_staff_res_given_mal_id(21517)
    parser = StaffParser(res.text)
    data = parser.build_dictionary()

    assert data["mal_id"] == 21517
    assert data["name"] == "Sora Amamiya"
    assert data["given_name"] == "天"
    assert data["family_name"] == "雨宮"
    assert data["alternate_name"] == []
    assert data["birthday"] == datetime.datetime(1993, 8, 28, 0, 0)
    assert (
        data["about"]
        == "Blood type: AB\nBirth place: Tokyo, Japan\n\nSora Amamiya was introduced to the seiyuu profession in high school by a friend who enjoyed anime. She decided to become a seiyuu after seeing the voice roles of Miyuki Sawashiro.\n\nIn 2011, Amamiya passed the 2nd Music Ray'n Super Seiyuu Audition and joined the talent agency. She debuted the following year voicing minor characters in Aikatsu!, Shinsekai yori, and Tonari no Kaibutsu-kun. Amamiya won her first lead role in Isshuukan Friends. in 2014. Later that year, she joined the unit TrySail with seiyuu Momo Asakura and Shiina Natsukawa, both of whom passed the same Music Ray'n audition.\n\nAmamiya was named a winner of the Best New Actress award in the 9th Seiyuu Awards. She is nicknamed Ten-chan, as her given name can also be read as \"Ten.\"\n\nBlog: http://ameblo.jp/amamiyasorablog/\nYoutube: https://www.youtube.com/channel/UCc4xpujLxnUBSI1XX-SdldQ\nTwitter: Amamiyastaff"
    )
    assert (
        data["staff_image"]
        == "https://cdn.myanimelist.net/images/voiceactors/2/64457.jpg"
    )


def test_natsukawa_shiina() -> None:
    """
    Dis function tests da information abou' Natsukawa Shiina, a seiyuu in da anime industry.
    It makes suwe dat hew ID is currect and dat hew name and biwthday awe currect.
    It also checks if dere is an image of hew and if she has any altewnat names. UwU
    """
    res = get_staff_res_given_mal_id(23405)
    parser = StaffParser(res.text)
    data = parser.build_dictionary()

    assert data["mal_id"] == 23405
    assert data["name"] == "Shiina Natsukawa"
    assert data["given_name"] == "椎菜"
    assert data["family_name"] == "夏川"
    assert data["alternate_name"] == []
    assert data["birthday"] == datetime.datetime(1996, 7, 18, 0, 0)
    assert (
        data["about"]
        == "Birth place: Chiba Prefecture, Japan\n\nBlog: ameblo.jp/natsukawashii..."
    )
    assert (
        data["staff_image"]
        == "https://cdn.myanimelist.net/images/voiceactors/2/40873.jpg"
    )


def test_momo_asakura() -> None:
    """
    Haii! This function checks the details about Asakura Momo, anothew amazing seiyuu in da anime industry!
    It confirms if her ID is correct and if her name and birthday are accurate. It also checks if there is an image of her and if she has any alternate names.
    Asakura-chan was born on July 18, 1996 in Fukuoka Prefecture, Japan!
    """
    res = get_staff_res_given_mal_id(26543)
    parser = StaffParser(res.text)
    data = parser.build_dictionary()

    assert data["mal_id"] == 26543
    assert data["name"] == "Momo Asakura"
    assert data["given_name"] == "もも"
    assert data["family_name"] == "麻倉"
    assert data["alternate_name"] == ["Mocho"]
    assert data["birthday"] == datetime.datetime(1994, 6, 25, 0, 0)
    assert data["about"] == "Blood type: O\nBirth place: Fukuoka Prefecture, Japan"
    assert (
        data["staff_image"]
        == "https://cdn.myanimelist.net/images/voiceactors/3/40866.jpg"
    )
