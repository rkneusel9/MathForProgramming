const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    try stdout.print("Using divTrunc and mod:{s}", .{"\n"});
    try stdout.print("    {d} {d} {d} {d}\n", .{ 33, 7, @divTrunc(33,7),  @mod(33,7)});
    try stdout.print("    {d} {d} {d} {d}\n", .{-33, 7, @divTrunc(-33,7), @mod(-33,7)});
    try stdout.print("    {d} {d} {d} {d}\n", .{ 33,-7, @divTrunc(33,-7), @mod(33,-7)});
    try stdout.print("    {d} {d} {d} {d}\n\n", .{-33,-7, @divTrunc(-33,-7),@mod(-33,-7)});
    try stdout.print("Using divTrunc and rem:{s}", .{"\n"});
    try stdout.print("    {d} {d} {d} {d}\n", .{ 33, 7, @divTrunc(33,7),  @rem(33,7)});
    try stdout.print("    {d} {d} {d} {d}\n", .{-33, 7, @divTrunc(-33,7), @rem(-33,7)});
    try stdout.print("    {d} {d} {d} {d}\n", .{ 33,-7, @divTrunc(33,-7), @rem(33,-7)});
    try stdout.print("    {d} {d} {d} {d}\n\n", .{-33,-7,@divTrunc(-33,-7), @rem(-33,-7)});

    try stdout.print("Using divFloor and mod:{s}", .{"\n"});
    try stdout.print("    {d} {d} {d} {d}\n", .{ 33, 7, @divFloor(33,7),  @mod(33,7)});
    try stdout.print("    {d} {d} {d} {d}\n", .{-33, 7, @divFloor(-33,7), @mod(-33,7)});
    try stdout.print("    {d} {d} {d} {d}\n", .{ 33,-7, @divFloor(33,-7), @mod(33,-7)});
    try stdout.print("    {d} {d} {d} {d}\n\n", .{-33,-7, @divFloor(-33,-7),@mod(-33,-7)});
    try stdout.print("Using divFloor and rem:{s}", .{"\n"});
    try stdout.print("    {d} {d} {d} {d}\n", .{ 33, 7, @divFloor(33,7),  @rem(33,7)});
    try stdout.print("    {d} {d} {d} {d}\n", .{-33, 7, @divFloor(-33,7), @rem(-33,7)});
    try stdout.print("    {d} {d} {d} {d}\n", .{ 33,-7, @divFloor(33,-7), @rem(33,-7)});
    try stdout.print("    {d} {d} {d} {d}\n\n", .{-33,-7,@divFloor(-33,-7), @rem(-33,-7)});
}

