#!/bin/sh

start() {
    cmd="cd docker; docker-compose up -d;"
    echo "\033[32m"$cmd
    eval $cmd
    return 0
}


stop() {
    cmd="cd docker; docker-compose stop;"
    echo "\033[32m"$cmd
    eval $cmd
    return 0
}


restart() {
    cmd="cd docker; docker-compose restart;"
    echo "\033[32m"$cmd
    eval $cmd
    return 0
}



case "$1" in

    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    *)
        echo "Usage: sh release.sh {import|start|stop|restart}" >&2
        exit 3
        ;;
esac