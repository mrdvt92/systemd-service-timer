#!/usr/bin/perl
use v5.10;
use strict;
use warnings;
use DateTime;

my $tmp = '/tmp/systemd-service-timer.tmp';
open my $fh, '>', $tmp;
say $fh DateTime->now;
close $fh;
