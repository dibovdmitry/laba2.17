#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import click
import os


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
@click.option("-p", "--path", help='Введите пункт назначения')
@click.option("-n", "--number", help='Введите номер рейса')
@click.option("-m", "--model", help='Введите модель самолёта')
def add(filename, path, number, model):
    if os.path.exists(filename):
        airplanes = load_airplanes(filename)
    else:
        airplanes = []

    airplanes.append(
        {
            'path': path,
            'number': number,
            'model': model,
        }
    )

    with open(filename, "w", encoding="utf-8") as fl:
        json.dump(airplanes, fl, ensure_ascii=False, indent=4)
    click.secho("Рейс добавлен")


@cli.command()
@click.argument('filename')
def display(filename):
    """
    Отобразить список маршрутов.
    """
    airplanes = load_airplanes(filename)
    if airplanes:
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^30} | {:^20} | {:^20} |'.format(
                "Пункт назначения",
                "Номер рейса",
                "Тип самолёта"
            )
        )
        print(line)

        for airplane in airplanes:
            print(
                '| {:<30} | {:>20} | {:<20} |'.format(
                    airplane.get('path', ''),
                    airplane.get('number', ''),
                    airplane.get('model', '')
                )
            )
        print(line)

    else:
        print("Маршруты не найдены")


@cli.command()
@click.argument('filename')
@click.option("-r", "--race", help="Введите нужный рейс")
def select(filename, sel):
    """
    Выбрать маршруты после заданного времени.
    """
    airplanes = load_airplanes(filename)
    result = []
    for airplane in airplanes:
        if airplane.get('path') <= sel:
            result.append(airplane)

    if result:
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^30} | {:^20} | {:^20} |'.format(
                "Пункт назначения",
                "№",
                "Время"
            )
        )
        print(line)

        for airplane in result:
            print(
                '| {:<30} | {:>20} | {:<20} |'.format(
                    airplane.get('path', ''),
                    airplane.get('number', ''),
                    airplane.get('model', '')
                )
            )
        print(line)

    else:
        print("Маршруты не найдены")


def load_airplanes(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == '__main__':
    cli()
