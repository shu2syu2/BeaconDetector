//
//  ContentView.swift
//  BeaconDetector
//
//  Created by S.S on 2022/10/16.
//

import Combine
import CoreLocation
import SwiftUI

class BeaconDetector: NSObject, ObservableObject, CLLocationManagerDelegate {
    var didChange = PassthroughSubject<Void, Never>()
    var locationManager: CLLocationManager?
    var lastDistance = CLProximity.unknown
    
    override init() {
        super.init()
        
        locationManager = CLLocationManager()
        locationManager?.delegate = self
        locationManager?.requestWhenInUseAuthorization()
    }
    
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization state : CLAuthorizationStatus) {
        if state == .authorizedWhenInUse {
            if CLLocationManager.isMonitoringAvailable(for: CLBeaconRegion.self) {
                if CLLocationManager.isRangingAvailable() {
                    startScanning()
                }
            }
        }
    }
    
    func startScanning() {
        let uuid = UUID(uuidString:
        "D546DF97-4757-47EF-BE09-3E2DCBDD0C77")!
        //"48534442-4C45-4114-48C0-1800FFFFFFFF")!
        let constraint = CLBeaconIdentityConstraint(uuid: uuid)
        //let constraint = CLBeaconIdentityConstraint(uuid: uuid, major: 10, minor: 20)
        let beaconRegion = CLBeaconRegion(beaconIdentityConstraint: constraint, identifier: "MyBeacon")
        
        locationManager?.startMonitoring(for: beaconRegion)
        locationManager?.startRangingBeacons(satisfying: constraint)
    }
    
    func locationManager(_ manager: CLLocationManager, didRange beacons: [CLBeacon], satisfying beaconConstraint: CLBeaconIdentityConstraint) {
        if let beacon = beacons.first {
            update(distance: beacon.proximity)
        }
        else {
            update(distance: .unknown)
        }
    }
    
    func update(distance: CLProximity) {
        lastDistance = distance
        didChange.send(())
    }
    
}

struct GreenButtonStyle: ViewModifier {
    func body(content: Content) -> some View {
        return content
        .foregroundColor(.white)
        .background(Color.green)
        .border(Color(red: 7/255,
                      green: 171/255,
                      blue: 67/255),
                width: 5)
    }
}

struct BigText: ViewModifier {
    func body(content: Content) -> some View {
        return content
        .font(Font.system(size:72, design: .rounded))
        .foregroundColor(.white)
        .frame(minWidth: 0, maxWidth: .infinity, minHeight: 0, maxHeight: .infinity)
    }
}

struct ContentView: View {
    @ObservedObject var detector = BeaconDetector()
    var body: some View {
        if detector.lastDistance == .immediate {
            Text("RIGHT NOW")
                .modifier(BigText())
                .background(Color.red)
                .edgesIgnoringSafeArea(.all)
        } else if detector.lastDistance == .near {
            Text("NEAR")
                .modifier(BigText())
                .background(Color.orange)
                .edgesIgnoringSafeArea(.all)
        } else if detector.lastDistance == .far {
            Text("FAR")
                .modifier(BigText())
                .background(Color.blue)
                .edgesIgnoringSafeArea(.all)
        } else {
            Text("UNkNOWN")
                .modifier(BigText())
                .background(Color.gray)
                .edgesIgnoringSafeArea(.all)
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
