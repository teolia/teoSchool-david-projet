var request = require('supertest');
var express = require('express');
var Rewire = require("rewire");
var sinon = require("sinon");
var redis = require('redis');

var app = Rewire("../webui.js")


var redisClientMock = {
    get: sinon.spy(function(something) {
        return "Get";
    }),
    hlen: sinon.spy(function(something) {
        return "HLen";
    }),
    on: sinon.spy(function() {})
};

var redisMock = {
    createClient: sinon.spy(function(something) {
        return redisClientMock;
    })
};

app.__set__('client', redisClientMock);
app.__set__('redis', redisMock);

describe('Index Page', function() {
    it("renders successfully", function(done) {
        request(app).get('/').expect(302, done);
    })
})

describe('json API', function() {
    it("returns data successfully", function(done) {
        request(app).get('/').expect(302, done);
    })
})